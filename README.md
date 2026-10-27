# Gaze Atlas · Eye-Tracking Game Open Database

An open, bilingual database of eye-tracking games and interactive research projects. Browse commercial titles, indie games, accessible gaze experiences, training activities, and academic prototypes, with images, descriptions, hardware details, and primary sources.

**Updated October 27, 2026:** 122 game records and 162 research publication records.

## Explore

- [English website](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/)
- [Chinese website](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/)
- [Research review and classification](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/review.html)

The website supports keyword search and filters for category, genre, design purpose, gaze role, hardware, interaction, and research population. Projects from UCSD PoNG and other institutions use the same classification; institutional provenance accompanies their sources.

## Research library

[English Research](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/research.html) · [中文研究论文](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/research.html)

Browse 162 publication records by topic, year, and publication type, with evidence-status labels. The October 27 update adds 85 non-duplicate records from an interaction-focused scoping review: 63 were assessed from full text and 22 remain provisional from public abstracts or HTML documentation. Each added record retains its coded eye signals, interaction roles, system names, and evidence cluster. Evidence-status labels reflect the contributor’s assessment records. This collection was contributed by [@WeiWu0115](https://github.com/WeiWu0115) in [PR #1](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/pull/1). Records include an original title, authors, venue, bilingual research focus, source links, and a DOI where identified. Related games are linked only when a high-confidence match is available.

Download [bilingual JSON](data/papers.json) or [CSV](data/papers.csv). Source-listing dates and metadata provenance are retained in the dataset. Original documents take precedence when correcting bibliographic details.

## Collection coverage

| Primary category | Records |
| --- | ---: |
| Commercial games | 34 |
| Indie & small games | 22 |
| Accessible gaze games | 16 |
| Research prototypes | 26 |
| Training & serious games | 22 |
| Research observation & datasets | 2 |
| **Total** | **122** |

Cross-cutting tags identify 24 records with Steam sources, 51 research-related records, 33 training records, seven VR records, and four documented award winners. Tags overlap across categories. Records represent individual games, prototypes, activity suites, and research environments.

## Open data

| Dataset | English | Chinese |
| --- | --- | --- |
| Main collection — 122 records | [JSON](en/data/games.json) · [CSV](en/data/games.csv) | [JSON](data/games.json) · [CSV](data/games.csv) |
| Review method and counts | [JSON](en/data/review-method.json) | [JSON](data/review-method.json) |

Records include stable IDs, titles, descriptions, categories, genres, design purposes, gaze roles, input methods, hardware, platforms, populations, evaluation details, edition context, image credits, and source links. Matching IDs connect the two language editions.

CSV files use UTF-8 with BOM for spreadsheet compatibility. Arrays and objects are stored as JSON-encoded strings. The main JSON file contains a `games` array.

## Sources and images

Documentation draws on official game pages, developers, hardware makers, research teams, original papers, and award records. Research details identify the study design, sample, and publication context.

Images are labeled as official screenshots, project media, collection overviews, app icons, or image placeholders. Each entry includes image provenance and rights information.

## Contribute

[Suggest a game or submit a correction](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/issues/new), or open a pull request. Include:

- A primary source describing the game and its interaction.
- Hardware, platform, edition, and access information.
- An image source, credit, and rights information.
- Research details and a verification date where applicable.

Use stable IDs and keep the English and Chinese editions, JSON, CSV, and review counts synchronized.

## Run locally

The website uses static HTML, CSS, and JavaScript. From the repository root, run:

```sh
python3 -m http.server 8765
```

Open [the English edition](http://localhost:8765/en/) or [the Chinese edition](http://localhost:8765/). GitHub Pages publishes the repository's `main` branch from the root directory.

## Licensing

Original descriptions, database arrangement, and original diagrams use [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribute **Gaze Atlas contributors**, retain source references, and identify modifications.

Website code uses the [MIT License](LICENSE). Third-party images, trademarks, papers, and games retain their original rights and licensing terms.

The donut-eye artwork is supplied by the project maintainer for the homepage; its rights remain with its contributor.

## Community contributions

Use **Contribute** in the website navigation to submit a game, open English or Chinese GitHub forms, read the guide, inspect automated checks, or view contributor credits.

- [Contribution hub](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/contribute.html)
- [Contributor credits](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/contributors.html)
- [Contribution guide](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/blob/main/CONTRIBUTING.md) · [Chinese guide](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/blob/main/CONTRIBUTING.zh-CN.md)
- [Catalog validation runs](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/actions/workflows/validate-data.yml)

For data changes, run `python3 scripts/sync_catalog.py`, `python3 scripts/validate_catalog.py`, and `python3 -m unittest discover -s tests` from the repository root. Accepted research, translation, code, and design contributions can be credited in `data/contributors.json` and each record’s optional `contributors` field.
