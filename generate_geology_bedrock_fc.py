import time

import httpx
from rdflib import (
    Graph,
    Namespace,
    RDF,
    DCAT,
    SDO,
    Literal,
    BNode,
    DCTERMS,
    XSD,
    RDFS,
    URIRef,
)
from shapely.geometry import box


dataset_json_url = "https://ogcapi.bgs.ac.uk/collections/bgsgeology625kbedrock?f=json"
url = "https://ogcapi.bgs.ac.uk/collections/bgsgeology625kbedrock/items?f=json&offset=0"

BGS = Namespace("http://data.bgs.ac.uk/id/")
GEOLOGY_MAP_DATASET = BGS.geology625k
FEATURE_COLLECTION_IRI = URIRef("http://data.bgs.ac.uk/id/geology625k/bedrock")
GEO = Namespace("http://www.opengis.net/ont/geosparql#")


def get_bbox(data):
    crs = data["crs"]
    bbox_coords = data["bbox"][0]
    bbox_geometry = box(*bbox_coords)
    wkt = bbox_geometry.wkt
    return f"<{crs}> {wkt}"


def generate():
    graph = Graph()

    response = httpx.get(dataset_json_url)
    response.raise_for_status()

    data = response.json()

    iri = FEATURE_COLLECTION_IRI
    graph.add((GEOLOGY_MAP_DATASET, RDFS.member, iri))
    graph.add((iri, RDF.type, GEO.FeatureCollection))

    name = Literal(data["title"])
    graph.add((iri, SDO.name, name))

    description = Literal(data["description"])
    graph.add((iri, SDO.description, description))

    keywords = [Literal(keyword) for keyword in data["keywords"]]
    for keyword in keywords:
        graph.add((iri, DCAT.keyword, keyword))

    bbox = get_bbox(data["extent"]["spatial"])
    geom = BNode()
    graph.add((iri, GEO.hasBoundingBox, geom))
    graph.add((geom, RDF.type, GEO.Geometry))
    graph.add((geom, GEO.asWKT, Literal(bbox, datatype=GEO.wktLiteral)))

    temporal_start = data["extent"]["temporal"]["interval"][0][0]
    temporal_end = data["extent"]["temporal"]["interval"][0][1]
    period_of_time = BNode()
    if temporal_start is not None:
        graph.add((iri, DCTERMS.temporal, period_of_time))
        graph.add((period_of_time, RDF.type, DCTERMS.PeriodOfTime))
        graph.add(
            (period_of_time, DCAT.startDate, Literal(temporal_start, datatype=XSD.date))
        )
    if temporal_start is not None and temporal_end is not None:
        graph.add(
            (period_of_time, DCAT.endDate, Literal(temporal_end, datatype=XSD.date))
        )

    graph.serialize(
        "spatial/geologymap/bedrock-feature-collection.ttl", format="longturtle"
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
