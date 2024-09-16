"""
Geochronology
"""

import time
from textwrap import dedent

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, SKOS


concept_scheme_data = """
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<http://data.bgs.ac.uk/ref/Geochronology>
    a skos:ConceptScheme ;
    dcterms:accessRights <http://data.bgs.ac.uk/ref/void> ;
    dcterms:created "2023-07-28"^^xsd:date ;
    dcterms:modified "2023-07-28"^^xsd:date ;
    dcterms:creator <http://data.bgs.ac.uk/ref/BritishGeologicalSurvey> ;
    skos:definition "The BGS Geochronology vocabulary."@en ;
    dcterms:identifier "http://data.bgs.ac.uk/ref/Geochronology"^^xsd:anyURI ;
    dcterms:publisher <http://data.bgs.ac.uk/ref/BritishGeologicalSurvey> ;
    skos:prefLabel "Geochronology"@en ;
    skos:historyNote "BGS GitHub repository"@en ;
.
"""


def main() -> None:
    starttime = time.time()

    try:
        graph = Graph()
        graph.parse("vocabularies/geochronology.nt")
        graph.parse(data=concept_scheme_data)

        concept_scheme = URIRef("http://data.bgs.ac.uk/ref/Geochronology")
        concepts = list(graph.subjects(RDF.type, SKOS.Concept))

        for concept in concepts:
            graph.add((concept, SKOS.inScheme, concept_scheme))
            graph.add((concept, SKOS.historyNote, Literal("From the BGS vocabularies GitHub repository.")))

        query = dedent(
            """
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            SELECT DISTINCT ?concept
            WHERE {
            ?concept a skos:Concept .
            FILTER NOT EXISTS {
                ?concept skos:broader ?parent_concept .
            }
            FILTER NOT EXISTS {
                ?parent_concept skos:narrower ?concept . 
            }
            }
        """
        ).strip()

        result = graph.query(query)

        for row in result:
            graph.add((concept_scheme, SKOS.hasTopConcept, row["concept"]))

        graph.serialize("vocabularies/geochronology.ttl", format="longturtle")

    finally:
        endtime = time.time() - starttime
        print(f"Completed in {endtime:0.2f} seconds")


if __name__ == "__main__":
    main()
