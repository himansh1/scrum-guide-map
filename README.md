# Scrum Guide Map

A phone-friendly visual reader for every page of the November 2020 Scrum Guide, with the supplied PSPO mock questions, a checked summary and tap-to-find shortcuts.

Live site: https://himansh1.github.io/scrum-guide-map/

## Version 3

- Terminal excerpts now keep introductory sentences with their complete following lists or topics. The Three planning topics endpoint includes the original Why, What and How headings and all four paragraphs. This repair covers 10 introduction groups and 42 endpoints, including Saved and exported cheat sheets.
- Complete Guide hierarchy: 14 PDF pages, 163 source blocks, 31 headings and 136 exact final passages.
- All 80 supplied questions, 112 selected answers and 320 original choices. The answer key is preserved; each question has a separate Guide check and source links. Ambiguous, qualified and non-Guide claims are labeled.
- All nine sections of the supplied one-page summary, organized into 25 reviewed cues. The original extracted summary remains accessible under Sources & checks.
- Keywords under map headings and 31 curated Find suggestions, including timeboxes, accountabilities, cancellation, release, Done and scaling.
- Supplementary links and short explanations from official Scrum.org resources.
- The Help page has been removed. Source attribution and validation remain under Sources & checks.

## Notes and offline use

Notes and saved passages stay in the current browser. Version 3 preserves the original node IDs and `scrum-guide-map-notes-v1` storage key. Export a JSON backup or an HTML cheat sheet from Saved. These personal notes are never sent to GitHub. The service worker caches the self-contained app after a successful online visit. External resource pages require a connection.

## Build and verification

Run `python3 build.py` to rebuild `index.html`, and `python3 verify_coverage.py` to verify complete original Guide coverage. Route, answer, keyword, summary and note-storage checks were run before publication. `coverage.json` records source hashes, normalization, coverage and the review method. The enrichment script uses local supplied inputs; the published data already contains the reviewed content.

Original Guide text is distinct from navigation labels, summary cues and question commentary. Layout whitespace is normalized, a line-wrapped “one-month” is joined, and printed page-number footers become metadata. Five values-practice sentences are split without changing their wording. The cleaned Q&A text removes an extra period after a question mark in Q59 and Q62; the DOCX wording is retained.

## Sources and rights

The Scrum Guide © 2020 Ken Schwaber and Jeff Sutherland, [official source](https://scrumguides.org/). The Guide and its visual adaptation are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The organization, navigation and commentary have been added; no endorsement by the authors or Scrum.org is implied.

The supplied mock, supplied summary and linked website resources retain their respective rights. The Guide's license does not automatically cover them. The supplied answer key is not an official Scrum.org answer key. Checks distinguish Guide rules, practical interpretation and statements not established by the Guide.
