# news-image-20261119 — The world in one day: Thursday 19 November 2026

Entry for make.fun's `news-image-20261119` bounty: a program that writes one
image summing up the world's news of Thursday 19 November 2026.

## The image

A newspaper front page, drawn programmatically with Pillow (`draw.py`):

- **Lead story:** the International Court of Justice rules 9–6 that Myanmar
  committed genocide against the Rohingya.
- **Also:** the first Trump–Xi–Putin three-way summit in Shenzhen and its joint
  peace declaration; Iran widening its attacks across the Gulf; COP31 talks in
  Antalya; the EU's proposed €45bn loan to Ukraine; violence spreading across
  Bangladesh; Voyager 1 reaching one light-day from Earth; plus a record
  $190.4m Van Gogh sale, the US Senate's 51–48 rejection of the Iran
  war-powers measure, and a migrant boat sinking off Senegal.

## How it runs

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No network is used and
both runs write identical bytes.

To regenerate the image: `python3 draw.py` (requires Pillow and the DejaVu
fonts). To test the entry: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts`.

## License

MIT — see `LICENSE`.
