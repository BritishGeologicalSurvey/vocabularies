"""
Add triples to pass VocPub validator.
"""

import time

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, SKOS


def main() -> None:
    starttime = time.time()

    try:
        graph = Graph()
        graph.parse("vocabularies/thesaurus_metadata.ttl")
        graph.parse("vocabularies/thesaurus.nt", format="ntriples")

        concepts = graph.subjects(RDF.type, SKOS.Concept)
        concept_scheme = graph.value(None, RDF.type, SKOS.ConceptScheme)
        top_concept = URIRef("http://data.bgs.ac.uk/id/GeoscienceThesaurus/Concept/0")

        # Fix top concept pointing to concept scheme with trailing slash.
        graph.remove(
            (
                URIRef("http://data.bgs.ac.uk/ref/GeoscienceThesaurus/"),
                SKOS.hasTopConcept,
                top_concept,
            )
        )
        graph.add((concept_scheme, SKOS.hasTopConcept, top_concept))

        for concept in concepts:
            graph.remove((concept, SKOS.inScheme, None))
            graph.add((concept, SKOS.inScheme, concept_scheme))

            if graph.value(concept, SKOS.definition, None) is None:
                label = graph.value(concept, SKOS.prefLabel, None)
                graph.add((concept, SKOS.definition, label))

            if (
                graph.value(concept, SKOS.broader, None) is None
                and graph.value(None, SKOS.narrower, concept) is None
            ):
                graph.add(
                    (
                        top_concept,
                        SKOS.narrower,
                        concept,
                    )
                )
                graph.add((concept, SKOS.broader, top_concept))

        graph.serialize("vocabularies/thesaurus.ttl", format="longturtle")

    finally:
        endtime = time.time() - starttime
        print(f"Completed in {endtime:0.2f} seconds")


if __name__ == "__main__":
    main()
