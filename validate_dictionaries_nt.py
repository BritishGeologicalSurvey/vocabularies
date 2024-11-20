from rdflib import Graph

graph = Graph()

errors = []

with open("dictionaries.nt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file.readlines()):
        lineno = i + 1
        try:
            graph.parse(data=line, format="ntriples")
        except Exception as err:
            errors.append(f"Failed to parse line {lineno}. {line}\nError: {err}")

graph.serialize("dictionaries.ttl", format="longturtle")

if errors:
    for error in errors:
        print(error)

    print(f"Total errors: {len(errors)}")
