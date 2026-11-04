# Scrum Guide Mind Map

[Open the mind map](https://himansh1.github.io/scrum-guide-map/)

A phone-friendly, tap-through reading companion for the complete **November 2020 Scrum Guide**, by Ken Schwaber and Jeff Sutherland.

The five main branches follow the Guide: fundamentals and theory, Scrum values, Scrum Team, Scrum events, and Scrum artifacts. Purpose, cover, contents, acknowledgements and licensing are included under **About the Guide**. Each final branch contains the original paragraph, list item or sentence, with its printed page reference.

## Features

- Hierarchical mind map with browser Back support and direct links to every branch.
- All 14 PDF pages, including the cover and printed pages 1–13.
- 136 terminal passages; all 163 source blocks accounted for, including 31 headings.
- Original page reader, full-branch reading view and optional search.
- Saved passages and notes stored only in the current browser.
- HTML cheat-sheet export and JSON backup/import. Notes are never uploaded to GitHub.
- Offline access after the first successful online load; look for **Offline ready**.

On Android, open the site in Chrome and choose **⋮ → Add to Home screen**. Clearing browser data can remove notes and offline files; export a backup to keep notes or move them between devices.

## Source fidelity

The supplied PDF was extracted page by page. The extraction is included as `guide-pages.json`; the ordered source blocks are in `blocks.json`. `coverage.json` records the source PDF SHA-256 and coverage counts.

Only layout whitespace is normalized, and the PDF's line-wrapped `one-month` is joined. Printed page-number footers become metadata. The paragraph describing the five values in practice is split into its five unchanged sentences. Navigation labels are editorial; leaf quotations preserve the Guide's wording. The source blocks reconstruct the complete extracted text after these normalizations.

Run `python3 verify_coverage.py` to verify coverage. The application is dependency-free. Rebuild the standalone HTML with `python3 build.py` after editing its source files. Serve this directory with a local HTTP server to test service-worker support.

## Attribution and license

**The Scrum Guide**, November 2020. © 2020 Ken Schwaber and Jeff Sutherland. Original source: [scrumguides.org](https://scrumguides.org/) and the [official 2020 English PDF](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf).

The Guide and this visual adaptation are licensed under [Creative Commons Attribution–ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/). This adaptation changes organization and presentation and adds navigation, offline access and local notes. It does not imply endorsement by the Guide's authors or Scrum.org. User-authored notes remain separate from the Guide.
