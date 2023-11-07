import time

from rdflib import Graph, RDF, SKOS


def fix_dataholdings():
    """
    Remove concept scheme declaration as it breaks Prez trying to list it in the vocabularies listing page.

    Error is: ValueError: Can't split 'http://data.bgs.ac.uk/ref/dataHolding/'

    Remove collection declaration as it doesn't make sense to list these as a SKOS collection.
    Each item in the collection also don't load correctly as they are not SKOS concepts.
    """
    filepath = "vocabularies/dataholdings.nt"
    fileformat = "ntriples"
    graph = Graph()
    graph.parse(filepath, format=fileformat)
    graph.remove((None, RDF.type, SKOS.ConceptScheme))
    graph.remove((None, RDF.type, SKOS.Collection))
    graph.serialize(filepath, fileformat, encoding="utf-8")


def fix_geology_map():
    """
    Remove concept scheme declarations.

    We use normal file and line processing here because rdflib cannot parse this file containing data with XML.
    """
    filepath = "vocabularies/625KGeologyMap_all.nt"
    lines = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file.readlines():
            if not "<http://www.w3.org/2004/02/skos/core#ConceptScheme>" in line:
                lines.append(line)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write("".join(lines))


def fix_bedding_surface_structure():
    """
    Vocab is defined as both concept scheme and collection.

    Remove the collection type declaration.
    """
    filepath = "vocabularies/simple-dictionaries/BeddingSurfaceStructure_scheme.nt"
    fileformat = "ntriples"
    graph = Graph()
    graph.parse(filepath, format=fileformat)
    graph.remove((None, RDF.type, SKOS.Collection))
    graph.serialize(filepath, fileformat, encoding="utf-8")


def fix_borehole_material_type():
    filepath = "vocabularies/simple-dictionaries/BoreholeMaterialType_scheme.nt"
    fileformat = "ntriples"
    graph = Graph()
    graph.parse(filepath, format=fileformat)
    graph.remove((None, RDF.type, SKOS.Collection))
    graph.serialize(filepath, fileformat, encoding="utf-8")


def fix_rockunitrank():
    filepath = "vocabularies/LexiconRockUnitName/RockUnitRank_scheme.nt"
    fileformat = "ntriples"
    graph = Graph()
    graph.parse(filepath, format=fileformat)
    graph.remove((None, RDF.type, SKOS.Collection))
    graph.serialize(filepath, fileformat, encoding="utf-8")


def main() -> None:
    starttime = time.time()

    try:
        fix_dataholdings()
        fix_geology_map()
        fix_bedding_surface_structure()
        fix_borehole_material_type()
        fix_rockunitrank()

    finally:
        endtime = time.time() - starttime
        print(f"Completed in {endtime:0.2f} seconds")


if __name__ == "__main__":
    main()
