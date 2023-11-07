from pathlib import Path

from rdflib import Graph

spatial_path = Path("spatial")
vocabularies_path = Path("vocabularies")

files = list(spatial_path.glob("**/*")) + list(vocabularies_path.glob("**/*"))
graph = Graph()
for file in files:
    if file.is_file() and file.name != ".DS_Store" and file.name != "625KGeologyMap_all.nt" and file.name != "dataholdings.nt":
        try:
            graph.parse(file)
        except Exception as err:
            raise RuntimeError(f"Failed to parse file {file.name}. {err}") from err

graph.serialize("compounded.ttl", format="longturtle")
