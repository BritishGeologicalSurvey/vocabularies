# BGS Vocabularies

This repository hosts the datasets of BGS controlled vocabularies in Linked Open Data form, serialised as N-Triples, for the purposes of bulk download for loading into a graph database/triplestore, and for publicly exposing the version history of the vocabularies.
Content is updated nightly.
The data is stored in BGS's own triplestore and is made available from there through an API at https://data.bgs.ac.uk, with user interface HTML pages also provided for some of the schemes.

## Repository Contents

`625KGeologyMap_all.nt` BGS Geology 625k (DiGMapGB -625) contains the triples for the map features; the triples for the concept scheme and BGS defined predicates and resource types are currently contained in `metadata/linked-data-mappings.nt`

`vocabularies/dataholding.nt` - Dataset Catalogue - contains a minimal set of triples for the items in our dataset catalogue, this consists of identifiers and a link to the landing page and is used primarily to handle PID and redirects.

`vocabularies/thesaurus.nt` - BGS Thesaurus of Geosciences - contains the complete set of triples for the BGS Thesaurus of Geosciences - describing the concept scheme and the concepts. ALl predicate and resource types are taken from common schemas (skos, dcterms).

`vocabularies/lexicon-named-rock-unit.nt` - BGS Lexicon of Named Rock Units -  contains the triples for the concepts; the triples for the concept scheme and BGS defined predicates and resource types are currently contained in `metadata/linked-data-mappings.nt`

`vocabularies/earth-material-class.nt` - Earth Material Class (BGS Rock Classification Scheme) -  contains the triples for the concepts; the triples for the concept scheme and BGS defined predicates and resource types are currently contained in `metadata/linked-data-mappings.nt`

`vocabularies/geochronology.nt` - BGS Geochronology - contains the triples for the concepts; the triples for the concept scheme and BGS defined predicates and resource types are currently contained in `metadata/linked-data-mappings.nt`

`metadata/linked-data-mappings.nt` contains the descriptions of some of the concept schemes above, description of all predicates and resource types used in the datasets (including capturing the labels of third party predicates), and alignments between BGS vocabulary terms and terms in third party vocabularies

## License

Thus repository's content are licensed under the [Open Government Licence 3.0 (OGL 3.0)](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## Contacts

*Vocabularies owner*: 

**Rachel Heaven**  

<https://www.bgs.ac.uk/staff/profiles/0639.html>
 

## Other Sources of Geoscience Vocabularies


### IUGS CGI Vocabularies

Server: https://cgi.vocabs.ga.gov.au/
Files: https://github.com/GeoscienceAustralia/cgi-vocabs (https://github.com/CGI-IUGS/cgi-vocabs)

### EARTh

https://vocabularyserver.com/cnr/ml/earth/en/index.php?tema=103230&/earth-sciences

### Linked Earth

Service down but files at - https://github.com/LinkedEarth/Ontology/ 

### ISPRAM

http://dati.isprambiente.it/ontology/core/#classes 

### INSPIRE    

https://inspire.ec.europa.eu/layer 
https://inspire.ec.europa.eu/glossary
https://inspire.ec.europa.eu/featureconcept
https://inspire.ec.europa.eu/codelist

### NERC Vocabulary Server NVS

http://vocab.nerc.ac.uk/

### Centre for Ecology and Hydrology (CEH)

https://vocabs.ceh.ac.uk/en/

### USGS

https://apps.usgs.gov/thesaurus/
https://volcanoes.usgs.gov/vsc/glossary/
https://water.usgs.gov/glossaries.html

### CSIRO

https://github.com/CSIRO-enviro-informatics/info-engineering
List of vocabs - https://csiro-enviro-informatics.github.io/info-engineering/cv.html 

### BRGM

https://data.geoscience.fr/ncl/

### GSWA

http://gswaprez.australiaeast.azurecontainer.io/vocprez

### GSQ

https://vocabs.gsq.digital/vocabulary/
https://github.com/geological-survey-of-queensland/vocabularies

### TNO

https://ontology.tno.nl/ (doesn't look like geoscience is in here)

### GBA (Austria)

https://schmar00.github.io/gba-thesaurus/ 

### GeoERA

https://github.com/schmar00/project-vocabularies
https://www.europe-geology.eu/data-and-services/vocabularies/ 

### WikiData

https://www.wikidata.org/wiki/Wikidata:Main_Page

