import time

import httpx
from rdflib import (
    Graph,
    Namespace,
    RDF,
    SDO,
    Literal,
    BNode,
    RDFS,
    URIRef,
)
from shapely.geometry import MultiPolygon, Polygon


url = (
    "https://ogcapi.bgs.ac.uk/collections/bgsgeology625kbedrock/items?f=json&offset={}"
)

BGS = Namespace("http://data.bgs.ac.uk/id/")
GEOLOGY_MAP_DATASET = BGS.geology625k
FEATURE_COLLECTION_IRI = URIRef("http://data.bgs.ac.uk/id/geology625k/bedrock")
FEATURE_TYPE = "Bedrock"
FEATURE_IRI = "http://data.bgs.ac.uk/id/geology625k/bedrock/{}"
GEO = Namespace("http://www.opengis.net/ont/geosparql#")
GEOLOGY_MAP_REF = Namespace("http://data.bgs.ac.uk/ref/625KGeologyMap/")


def get_wkt(data):
    geom_type = data["type"]
    coords = data["coordinates"]

    if geom_type == "MultiPolygon":
        geom = MultiPolygon([Polygon(coord[0]) for coord in coords])
    else:
        raise ValueError(f"Handling of geometry type {geom_type} not implemented.")

    return geom.wkt


def generate():
    graph = Graph()

    per_page = 100
    page_num = 0

    graph = Graph()

    while True:
        print(f"Processing page {page_num + 1}.")
        response = httpx.get(url.format(page_num * per_page))
        response.raise_for_status()

        data = response.json()

        features = data["features"]

        if features:
            for feature in features:
                feature_id = feature["id"]
                iri = URIRef(FEATURE_IRI.format(feature_id))
                graph.add((iri, RDF.type, GEO.Feature))
                graph.add(
                    (iri, SDO.name, Literal(f"{FEATURE_TYPE} Feature {feature_id}"))
                )
                graph.add((FEATURE_COLLECTION_IRI, RDFS.member, iri))

                try:
                    wkt = get_wkt(feature["geometry"])
                except Exception as err:
                    raise RuntimeError(
                        f"Error processing feature {feature_id} on page {page_num + 1}"
                    ) from err

                geom_bnode = BNode()
                graph.add((iri, GEO.hasGeometry, geom_bnode))
                graph.add((geom_bnode, RDF.type, GEO.Geometry))
                graph.add(
                    (geom_bnode, GEO.asWKT, Literal(wkt, datatype=GEO.wktLiteral))
                )

                properties = feature["properties"]

                if properties:
                    for key, value in properties.items():
                        property_bnode = BNode()
                        graph.add((iri, SDO.additionalProperty, property_bnode))
                        graph.add((property_bnode, RDF.type, SDO.PropertyValue))
                        graph.add((property_bnode, SDO.name, Literal(key)))
                        graph.add((property_bnode, SDO.value, Literal(value)))

                    lex = properties["LEX"]
                    if lex is not None and lex != "" and lex != "NOT APPLICABLE":
                        graph.add(
                            (
                                iri,
                                GEOLOGY_MAP_REF.hasLexicon,
                                URIRef(
                                    f"http://data.bgs.ac.uk/id/Lexicon/NamedRockUnit/{lex}"
                                ),
                            )
                        )

                    rcs = properties["RCS"]
                    if rcs is not None and rcs != "" and rcs != "NOT APPLICABLE":
                        graph.add(
                            (
                                iri,
                                GEOLOGY_MAP_REF.hasEarthMaterialClass,
                                URIRef(f"http://data.bgs.ac.uk/id/RockClass/{rcs}"),
                            )
                        )

                    rank = properties["RANK"]
                    if rank is not None and rank != "" and rank != "NOT APPLICABLE":
                        graph.add(
                            (
                                iri,
                                GEOLOGY_MAP_REF.hasRank,
                                URIRef(
                                    f"http://data.bgs.ac.uk/id/625KGeologyMap/Rank/{rank}"
                                ),
                            )
                        )

            page_num += 1
        else:
            # We've reached the end of the feature collection.
            break

    graph.serialize(
        "spatial/geologymap/bedrock-features.nt", format="ntriples", encoding="utf-8"
    )


def main() -> None:
    starttime = time.time()

    try:
        generate()

    finally:
        endtime = time.time() - starttime
        print(f"Completed in {endtime:0.2f} seconds")


if __name__ == "__main__":
    main()
