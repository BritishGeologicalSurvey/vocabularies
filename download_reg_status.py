import time

from rdflib import Graph


def main() -> None:
    starttime = time.time()

    try:
        graph = Graph()
        graph.parse("https://linked.data.gov.au/def/reg-statuses", format="text/turtle")
        graph.serialize(
            "vocabularies/reg-status.nt", format="ntriples", encoding="utf-8"
        )

    finally:
        endtime = time.time() - starttime
        print(f"Completed in {endtime:0.2f} seconds")


if __name__ == "__main__":
    main()
