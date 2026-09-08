# BGS Vocabularies

Datasets of British Geological Survey controlled vocabularies in Linked Open Data form,
serialised as [N-Triples](https://www.w3.org/TR/n-triples/). Published here for bulk
download into a graph database or triplestore, and to expose the version history of the
vocabularies publicly.

The same data is served through an API at [data.bgs.ac.uk](https://data.bgs.ac.uk), with
[HTML user interface pages](https://vocab.bgs.ac.uk) for some of the schemes. Use the API for individual concept
lookups and content negotiation; use this repository when you want the whole dataset.

## How this repository is maintained

The vocabularies are maintained in relational databases at BGS (the source of truth) and are exported nightly into our triplestore, and the nt files into an internal git repository which is mirrored on github.

Commits and pull requests made directly on github cannot be merged, otherwise the mirror will stop updating.
Please raise an [issue](../../issues) instead, or contact one of the data managers below.

## Versioning and releases

Releases are calendar-versioned as `YYYY.MM` and cut monthly on the 15th, tagged both
internally and here. Each release is a snapshot of the vocabularies on that date, with
per-file statement counts and a diff summary against the previous release in the notes.

Before this repository existed, releases were manual. Two earlier versions of the BGS
Lexicon are recorded in the BGS data catalogue:

- September 2017 — <http://data.bgs.ac.uk/id/dataHolding/13607204>
- April 2019 — <http://data.bgs.ac.uk/id/dataHolding/13607461>

Quarterly `YYYY.MM` releases ran from July 2024; the cadence moved to monthly in
September 2026.

## Repository contents

### File naming conventions

Files are grouped by vocabulary. Within each group the suffix tells you what the file
holds:

| Suffix | Contents |
|:--|:--|
| *(none)* | The concepts themselves — the main dataset for that vocabulary |
| `-scheme-only` | Just the `skos:ConceptScheme` description, without the concepts. Useful for building a catalogue without loading millions of triples |
| `-predicates` | BGS-defined predicates and resource types used by that vocabulary |
| `-alignments-<target>` | `skos:exactMatch` / `closeMatch` links to an external vocabulary (`dbpedia`, `cgi`, `inspire`) |
| `-colours` | Presentation colours (Geochronology only) |

Predicate and resource-type definitions not carried in a per-vocabulary `-predicates`
file are in `metadata/linked-data-mappings.nt`.

### Vocabularies

**`vocabularies/GeoscienceThesaurus/`** — BGS Thesaurus of Geosciences. Complete and
self-contained: the concept scheme and the concepts, using only SKOS and Dublin Core
predicates.

**`vocabularies/LexiconNamedRockUnit/`** — BGS Lexicon of Named Rock Units. The largest
vocabulary here. `RockUnitRank` gives the lithostratigraphic hierarchy (group, formation,
member and so on).

**`vocabularies/EarthMaterialClass/`** — BGS Rock Classification Scheme.
`RockName` and `RockComposite` cover named lithologies and composite materials;
`RockClassAll` is the combined set.

**`vocabularies/Geochronology/`** — BGS Geochronology, with `GeochronologyRank` for the
chronostratigraphic hierarchy and alignments to the IUGS CGI, INSPIRE and DBpedia
timescales.

**`vocabularies/625kGeologyMap/`** — BGS Geology 625k (DiGMapGB-625). Triples for the map
features themselves; the concept scheme and predicates are in
`metadata/linked-data-mappings.nt`.

**`vocabularies/DataCataloguePID/`** — Dataset catalogue. A minimal set of triples —
identifiers plus a link to the landing page — used to resolve persistent identifiers and
handle redirects.

**`vocabularies/simple-dictionaries/`** — Smaller controlled lists used in BGS data
capture, currently bedding surface structure and borehole material type.

### Supporting directories

**`metadata/`** — `linked-data-mappings.nt` holds concept scheme descriptions, all
predicate and resource-type definitions used across the datasets (including labels for
third-party predicates), and alignments to external vocabularies. `ref-predicates.nt` and
`reg-status.nt` carry reference predicates and registry status.

**`modified/`** — Data management purposes only. Contains diff-like modifications to triples used to manage the nightly deletions and additions to the triplestore. Format is N-Triples-like, hence the `.ntx` extension. Not valid N-Triples; do not load into a triplestore. 

## Loading the data

The files are plain N-Triples, so they concatenate. To load everything into a triplestore:

```bash
cat vocabularies/*/*.nt metadata/*.nt > bgs-vocabularies.nt
```

Or load a single vocabulary, for example the Thesaurus:

```bash
curl -sL https://raw.githubusercontent.com/BritishGeologicalSurvey/vocabularies/main/vocabularies/GeoscienceThesaurus/GeoscienceThesaurus.nt \
  | rdfpipe -i nt -o turtle - > thesaurus.ttl
```

Note that `vocabularies/625kGeologyMap/625kGeologyMap_all.nt` is close to 100 MB. If you
are cloning only to obtain the data, `git clone --depth 1` will save you a great deal of
time and disk.

## Related reading

- [The BGS Rock Classification Scheme as linked data](https://doi.org/10.1016/j.acags.2023.100131) — Applied Computing and Geosciences
- [Exposing and resolving persistent identifiers on the web](https://britishgeologicalsurvey.github.io/open%20data/persistent-identifiers/) — BGS developer blog

## Licence

Content in this repository is licensed under the
[Open Government Licence 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## Contacts

[Rachel Heaven](https://www.bgs.ac.uk/people/heaven-rachel-2/) — Lead developer, Thesaurus data manager

[Tim McCormick](https://www.bgs.ac.uk/people/mccormick-timothy/) — Lexicon, Geochronology and Rock Classification Scheme data manager

## Other sources of geoscience and environmental vocabularies

| | |
|:--|:--|
| GEMET | <https://www.eionet.europa.eu/gemet> |
| SWEET ontology | <https://bioportal.bioontology.org/ontologies/SWEET> |
| IUGS CGI | <https://cgi.vocabs.ga.gov.au/> — files at <https://github.com/CGI-IUGS/cgi-vocabs> |
| EARTh | <https://vocabularyserver.com/cnr/ml/earth/en/index.php?tema=103230&/earth-sciences> |
| Linked Earth | <https://github.com/LinkedEarth/Ontology/> (service currently down) |
| ISPRA | <http://dati.isprambiente.it/ontology/core/#classes> |
| INSPIRE | <https://inspire.ec.europa.eu/layer> · [glossary](https://inspire.ec.europa.eu/glossary) · [feature concepts](https://inspire.ec.europa.eu/featureconcept) · [codelists](https://inspire.ec.europa.eu/codelist) |
| NERC Vocabulary Server | <http://vocab.nerc.ac.uk/> |
| UKCEH | <https://vocabs.ceh.ac.uk/en/> |
| USGS | [thesaurus](https://apps.usgs.gov/thesaurus/) · [volcano glossary](https://volcanoes.usgs.gov/vsc/glossary/) · [water glossaries](https://water.usgs.gov/glossaries.html) |
| CSIRO | <https://csiro-enviro-informatics.github.io/info-engineering/cv.html> |
| BRGM | <https://data.geoscience.fr/ncl/> |
| GSWA | <http://gswaprez.australiaeast.azurecontainer.io/vocprez> |
| GSQ | <https://vocabs.gsq.digital/vocabulary/> — files at <https://github.com/geological-survey-of-queensland/vocabularies> |
| GBA (Austria) | <https://schmar00.github.io/gba-thesaurus/> |
| GeoERA | <https://www.europe-geology.eu/data-and-services/vocabularies/> |
| Wikidata | <https://www.wikidata.org/wiki/Wikidata:Main_Page> |