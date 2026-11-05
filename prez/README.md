# Published knowledge graph

Generated nightly by `tools/build_kg.py` in triples-ql-views from the files in this repository. **Do not edit by hand.**

Catalogue: <http://data.bgs.ac.uk/ref/BGSVocabularies> BGS Vocabularies ([`catalogue.ttl`](catalogue.ttl), version 2026-11-03T11:14:26Z)

| Vocabulary | Concept scheme (named graph) | Concepts | Triples | Version |
|:--|:--|--:|--:|:--|
| [BGS Geoscience Thesaurus](vocabs/GeoscienceThesaurus.ttl) | <http://data.bgs.ac.uk/ref/GeoscienceThesaurus> | 6127 | 66866 | 2026-11-03T11:14:26Z |
| [BGS Lexicon of Named Rock Units](vocabs/NamedRockUnit.ttl) | <http://data.bgs.ac.uk/ref/Lexicon/NamedRockUnit> | 18913 | 341189 | 2026-11-03T11:14:26Z |
| [Lexicon Rock Unit Rank](vocabs/RockUnitRank.ttl) | <http://data.bgs.ac.uk/ref/Lexicon/RockUnitRank> | 86 | 861 | 2026-11-03T11:14:26Z |
| [Lexicon Type Locality Type](vocabs/TypeLocalityType.ttl) | <http://data.bgs.ac.uk/ref/Lexicon/TypeLocalityType> | 4 | 49 | 2026-11-03T11:14:26Z |
| [Lexicon Source Reference Type](vocabs/SourceReferenceType.ttl) | <http://data.bgs.ac.uk/ref/Lexicon/SourceReferenceType> | 7 | 76 | 2026-11-03T11:14:26Z |
| [Geochronology Division](vocabs/Geochronology.ttl) | <http://data.bgs.ac.uk/ref/Geochronology/Division> | 423 | 6681 | 2026-11-03T11:14:26Z |
| [Geochronology Rank](vocabs/GeochronologyRank.ttl) | <http://data.bgs.ac.uk/ref/Geochronology/Rank> | 17 | 164 | 2026-11-03T11:14:26Z |
| [The BGS Rock Classification Scheme](vocabs/RockClassAll.ttl) | <http://data.bgs.ac.uk/ref/EarthMaterialClass/RockClassAll> | 3774 | 43200 | 2026-11-03T11:14:26Z |
| [Rock Classification Scheme - single rock types sub-scheme](vocabs/RockName.ttl) | <http://data.bgs.ac.uk/ref/EarthMaterialClass/RockName> | 3113 | 35870 | 2026-11-03T11:14:26Z |
| [Rock Classification Scheme - composite rock types sub-scheme](vocabs/RockComposite.ttl) | <http://data.bgs.ac.uk/ref/EarthMaterialClass/RockComposite> | 655 | 8013 | 2026-11-03T11:14:26Z |
| [Rock Classification Scheme - dummy rock classes sub-scheme](vocabs/RockDummy.ttl) | <http://data.bgs.ac.uk/ref/EarthMaterialClass/RockDummy> | 6 | 75 | 2026-11-03T11:14:26Z |
| [BGS Organisations](vocabs/Organisations.ttl) | <http://data.bgs.ac.uk/ref/org> | 3 | 60 | 2026-11-03T11:14:26Z |
| [BGS Licensing Actions](vocabs/LicensingActions.ttl) | <http://data.bgs.ac.uk/ref/licensing/action/> | 4 | 54 | 2026-11-03T11:14:26Z |
| [BeddingSurfaceStructure](vocabs/BeddingSurfaceStructure.ttl) | <http://data.bgs.ac.uk/ref/BeddingSurfaceStructure> | 21 | 182 | 2026-11-03T11:14:26Z |
| [BoreholeMaterialType](vocabs/BoreholeMaterialType.ttl) | <http://data.bgs.ac.uk/ref/BoreholeMaterialType> | 20 | 174 | 2026-11-03T11:14:26Z |

| Other dataset | Named graph | Triples | Version |
|:--|:--|--:|:--|
| [BGS discovery metadata (data holdings)](graphs/DiscoveryMetadata.ttl) | <http://data.bgs.ac.uk/ref/DiscoveryMetadata> | 7995 | 2026-11-05T12:45:53Z |
| [BGS Geology 1:625 000 map units](graphs/625kGeologyMap.ttl) | <http://data.bgs.ac.uk/ref/625KGeologyMap> | 237119 | 2026-11-03T11:14:26Z |
| [Registry statuses (AGLDWG)](graphs/RegistryStatuses.ttl) | <http://data.bgs.ac.uk/ref/reg-statuses> | 167 | 2026-11-03T11:14:26Z |

Labels: [`background/labels.ttl`](background/labels.ttl) (8186 triples), loaded into the `http://background` graph.

`manifest.ttl` is a [KGM manifest](https://kurrawong.github.io/kgm/guide/manifests/): `kgm sync` loads each vocabulary into its own named graph for Prez v4. This directory can also be used as prez-lite's `data/` directory as-is.
