import time
from textwrap import dedent

from rdflib import Graph, URIRef, Literal, SDO, SKOS


def main() -> None:
    starttime = time.time()

    try:
        gts_graph = Graph()
        gts_graph.parse(
            "https://raw.githubusercontent.com/GeoscienceAustralia/cgi-vocabs/bc48b3b81727fb8681c5b6c833b41d46c13104aa/vocabularies/ics/gts-chart-colours.ttl",
            format="text/turtle",
        )

        geochrono_graph = Graph()
        geochrono_graph.parse(
            "vocabularies/Geochronology/geochronology_alignments_cgi.nt",
            format="ntriples",
        )

        graph = Graph()

        def get_colour(iri: URIRef, graph: Graph) -> str | None:
            query = dedent(
                f"""
                PREFIX : <http://resource.geosciml.org/classifier/ics/gts-chart-colours/>
                PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

                SELECT ?colour
                WHERE {{
                    <{iri}> skos:notation ?colour .

                    FILTER(datatype(?colour) = :RGBHex)
                }}
            """
            )
            result = graph.query(query)

            for row in result:
                return str(row.colour)

        for s, _, o in geochrono_graph.triples((None, SKOS.exactMatch, None)):
            colour = get_colour(o, gts_graph)
            if colour is not None:
                graph.add((s, SDO.color, Literal(colour)))
            else:
                print(f"No colour found for {s} to {o}")

        graph.serialize(
            "vocabularies/Geochronology/geochronology_colours.nt",
            format="ntriples",
            encoding="utf-8",
        )

    finally:
        endtime = time.time() - starttime
        print(f"Completed in {endtime:0.2f} seconds")


if __name__ == "__main__":
    main()
