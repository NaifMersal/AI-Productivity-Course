# بناء مساعدك الذكي الخاص — AI at Work

Hands-on SDAIA workshops (Arabic, RTL) that teach people to turn the work they repeat into
reusable AI workflows. One shared library of decks, one small page per workshop, no build
step. The root [`index.qmd`](index.qmd) is the portal.

| Workshop | Page | Length | Guide |
|---|---|---|---|
| Building Your Own AI Assistant — office professionals | [`office.qmd`](office.qmd) | ≈2.5 hrs, online | [`outline.md`](outline.md) |
| Building Your Own AI Assistant — faculty | [`ksu.qmd`](ksu.qmd) | ≈2.5 hrs, online | [`outline.md`](outline.md) |
| Building Your Own AI Assistant — government | [`gov5.qmd`](gov5.qmd) | 5 days, in person | [`outline-gov5.md`](outline-gov5.md) |
| Academic Productivity & Innovation — faculty | [`edu5.qmd`](edu5.qmd) | 5 days, in person | [`outline-edu5.md`](outline-edu5.md) |

## How it's organized

Every `.qmd` is the real thing. Open it and edit it — there is no generator and no
template/generated split.

- **`slides/`** — the **concept** library, flat and shared by every workshop. A concept deck
  explains one idea and shows it working: the instructor demo and the closing knowledge check
  stay here. Editing a concept once updates every workshop.
- **`exercises/`** — the **exercise** library, also flat. This is where workshops differ. One
  file per drill: `exercises/handover.qmd` when every track runs the same one,
  `exercises/handover_gov5.qmd` when a track needs its own.
- **`data/`** — sample files for the exercises. The root is neutral and shared; `data/gov/` and
  `data/edu/` carry track-specific material.
- **the workshop pages** — a workshop is an index page: title, duration, and which concepts
  and exercises it lists, in what order, for how long. Each day table pairs them: an **العرض**
  column and a **المختبر** column.
- **the outlines** — one instructor guide per delivery format.

Neither library has per-audience subfolders. A subfolder is a licence to duplicate, and the
same idea ends up taught twice under two flavours with neither one maintained. The
concept/exercise split is not an audience split; it is what makes one *not* necessary.

**What varies between workshops is three things:** the workshop page, the **intro deck** it
opens with (`overview.qmd`, `intro_gov5.qmd`, `intro_edu5.qmd`), and **the exercises it runs**. The
intro deck carries the arc, the room rules and the promised outcome, and names the two safety
rules — it teaches no concept. Everything in `slides/` is written so an office employee, a
government employee and a faculty member all recognize the example. A **concept** deck that
must carry audience flavour has to be listed in the **flavour register** in
[`CLAUDE.md`](CLAUDE.md); an unregistered one that drifts flavoured is a defect. Exercises are
exempt — flavour is their job.

Adding a workshop: copy a workshop page, write its intro deck, pick or write its exercises, change
the day tables, add a row to `index.qmd`.

## Rendering slides

This project uses [Quarto](https://quarto.org/). The project config (`_quarto.yml`) lives at
the **repo root** and applies SDAIA branding globally; run all commands from the repo root.

```bash
quarto render                          # render everything into output/ (gitignored)
quarto render slides/cowork_intro.qmd  # one deck
quarto preview slides/cowork_intro.qmd # live reload
```

Render, screenshot, and verify branding and overflow:

```bash
python .claude/skills/author-verify-slides/driver.py slides/<deck>.qmd --all --reveal-all
```

## Project structure

- **`index.qmd`** — portal linking every workshop, every concept deck and every exercise.
- **`slides/`** — the flat concept library, including the three intro decks.
- **`exercises/`** — the flat exercise library. Mostly revealjs decks; the three printables
  (`capstone_worksheet`, `adoption_plan`, `gov5_worksheet`) are `format: html`.
- **`data/`** — sample files. Root is neutral; `data/gov/` and `data/edu/` are track-specific.
- **`assets/`** — instructor extras (the `.skill` bundle, deck screenshots). Not a deck source.
- **`office.qmd`**, **`ksu.qmd`**, **`gov5.qmd`**, **`edu5.qmd`** — the workshop pages.
- **`outline.md`**, **`outline-gov5.md`**, **`outline-edu5.md`** — instructor guides.
- **`_quarto.yml`** / **`slides_template/assets/`** — root Quarto config and SDAIA brand assets.
- **`notes/`** — **gitignored**, and not in this repository. It is the author's private
  working material: the planning notes, the Arabic voice style guide, the grounding packs
  behind every tool/law/product claim that reaches a slide, and the SDAIA dictionary. Several
  rules in [`CLAUDE.md`](CLAUDE.md) cite it. On a fresh clone those files are absent — ask the
  author for them rather than guessing what they said.
- **`scripts/make_redirects.py`** — runs automatically after every render (`post-render` in
  `_quarto.yml`) and writes redirect stubs so links to the old
  `office-workshop-ar/…` and `ksu-workshop/…` URLs land on the new pages. Its deck list is
  **pinned**, not globbed: only the nine decks that actually published under those old paths
  get stubs. When one of those nine moves, record where it went in the script's `CURRENT_PATH`
  map; otherwise it warns at render time.
