# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Layout

This repo builds SDAIA workshops from a **single set of templates + a JSON config**, so
deck *structure* is authored once and only the *examples/data* change per workshop. A root
`index.qmd` is the **portal** that links the generated offerings (URLs mirror the folder
paths, so keep them stable).

**Source of truth (committed):**
- `templates/workshop/` — the shared, structural decks: `index.qmd` (run-of-show) and
  `slides/*.qmd`. These hold the slide scaffolding **and the concept slides authored inline**,
  with placeholders where per-workshop examples go. Because `build.py` renders the same
  templates for every workshop, concepts are single-sourced across workshops here.
- `config/workshops.json` — one entry per workshop: its `out_dir`, a `vars` map (inline
  strings) and a `fragments` map (example-block files).
- `examples/<id>/` — the per-workshop swappable layer: `fragments/*.qmd` (example slide
  blocks), `data/*` (hands-on sample files), and `outline.md` (instructor outline, copied
  verbatim).
- `build.py` — generates each workshop from the above.
- `slides_template/`, `_quarto.yml` — shared SDAIA branding + Quarto config at the repo
  root, applied globally to every deck.
- `prompts/`, `notes/` — shared prompt guides/templates and loose planning notes.

**Generated (gitignored, produced by `build.py`):**
- `ksu-workshop/` — the only current workshop: "Building Your Own AI Assistant" (KSU
  faculty, half-day, Claude Cowork; academic examples). **Never edit it directly** — edit
  `templates/` or `examples/ksu/` and re-run `build.py`.

### The build system

`python build.py` reads `config/workshops.json` and, for each workshop, renders
`templates/workshop/**` into `<out_dir>/` while substituting two placeholder kinds, then
copies `examples/<id>/data/` and `examples/<id>/outline.md`:

- `{{ key }}` → `vars[key]` (an inline string). Does **not** touch Quarto shortcodes
  `{{< … >}}`.
- `<!-- EXAMPLE: key -->` (a whole line) → the contents of
  `examples/<id>/fragments/<fragments[key]>` (a multi-slide example block).

The build **fails loudly** if any placeholder lacks a value (content is never silently
dropped) and warns on unused vars/fragments. **Adding a workshop** = a new entry in
`config/workshops.json` + an `examples/<id>/` folder (fragments + data + outline) + a
portal row in the root `index.qmd`; no deck is forked.

### Concepts and examples

The foundation concepts (Two Layers, context, context window, **Project**, script, RICE,
advanced moves, Newspaper Test, grounding, **Connectors/MCP**) are authored **inline in the
template decks** under `templates/workshop/slides/` — those decks are the canonical wording.
Since `build.py` renders the same templates for every workshop, editing a concept once
updates every workshop — keep concept edits in the templates, never in a generated
`<id>-workshop/` copy. The **per-workshop** material (worked examples, sample prompts,
demos) is the only thing that varies, and it lives in `examples/<id>/fragments/` (pulled in
via `<!-- EXAMPLE: key -->`) plus the `vars` strings in `config/workshops.json`.

**Arabic:** `templates/workshop-ar/` is a full parallel template tree (selected via the
`template` key in `config/workshops.json`). Any structural or concept edit to
`templates/workshop/` must be mirrored there, and any new `{{ var }}` needs an entry in
**all three** workshop configs.

## Project Overview

**Building Your Own AI Assistant** — a half-day (~4.5 hr), hands-on workshop teaching **KSU
faculty** to use AI as a permanent member of their team (not as a search engine). By the
end each participant has a working **AI assistant they set up themselves** plus 2–3
automations on their own academic work, framed around **the recurring tasks worth handing
off**. Decks describe what the session does — they never promise hours saved or sell an
outcome.

**Hands-on tool:** **Claude Cowork** (Anthropic's desktop agent) — chosen because it is the
fastest to set up. Concepts stay **portable** (ChatGPT, Gemini, Claude, NotebookLM named as
alternatives). The audience is non-technical: **nobody writes code.**

The workshop is delivered **online**. The delivery loop is **Show** (instructor runs a real
task end to end) → **Mirror** (everyone repeats a small piece at the same time, from a
provided prompt and file) → **Take home** (the same task on their own work, from the
recipe). All hands-on agent work runs on copies of files in a **staging folder**.

### Key Files
- `examples/ksu/outline.md` — the KSU workshop outline (sessions, schedule, activities). Primary doc.
- `templates/workshop/slides/*.qmd` — the structural SDAIA-branded reveal.js decks, with the
  concept slides authored inline. **Canonical** wording for every concept (two layers,
  context, Project, script, Skill, Schedule/Cron, Connector/MCP, blast radius).
- `templates/workshop-ar/slides/*.qmd` — the Arabic parallel tree; mirror all edits here.
- `config/workshops.json` + `build.py` — the generator (see "The build system").
- `_quarto.yml` — Quarto project config at the **repo root** (global SDAIA branding; renders
  the source tree into repo-root `output/`).
- `slides_template/assets/` — SDAIA brand assets (`sdaia.scss`, logo/icon SVGs, `splash.lua`,
  `favicon.html`) referenced globally by `_quarto.yml`.
- `examples/ksu/data/` — datasets used in hands-on activities (e.g. `grades.csv`, sample essays).
- `prompts/`, `notes/` — prompt guides/templates and loose planning notes.

## Slides

Slides are SDAIA-branded Quarto reveal.js decks. Branding is applied globally in the
root `_quarto.yml`, so each deck's front matter stays minimal
(`title` / `subtitle` / `date` / `format: revealjs`). Author, render, preview,
screenshot, and visually verify them with the **`author-verify-slides`** skill —
branding and Quarto patterns are constant across SDAIA slide projects.

**Always run `python build.py` first** (it regenerates the gitignored `ksu-workshop/` from
the templates), then run Quarto from the repo root (Quarto finds `_quarto.yml` there and
mirrors the source path into `output/`, e.g. `ksu-workshop/slides/foo.qmd` →
`output/ksu-workshop/slides/foo.html`):

- Build the workshops: `python build.py`
- Render one deck: `quarto render ksu-workshop/slides/<deck>.qmd`
- Render all decks: `quarto render`
- Preview with live reload: `quarto preview ksu-workshop/slides/<deck>.qmd`
- Render + screenshot + verify branding/overflow:
  `python .claude/skills/author-verify-slides/driver.py ksu-workshop/slides/<deck>.qmd --all --reveal-all`

Because the rendered deck is generated, **fix content in `templates/` or `examples/ksu/`,
then re-run `build.py`** — edits to `ksu-workshop/` are overwritten. `output/` is gitignored.

## Core Teaching Framework

**The Two Layers** (the keystone, introduced in Session 1) — the mental model everything
else hangs off. The **model layer** is a "brain in a jar": stateless, knows nothing about
you, just predicts the next word, forgets everything when a request ends. The **app layer**
is the "office around the brain": it stores your info in a directory and **re-sends the
relevant context on every request**. Once learners see this, the working directory, Skills,
and grounding stop being magic — they're all the app getting smarter about *what to re-send*.
The Two Layers concept slides live inline in
`templates/workshop/slides/how_ai_works_and_rice.qmd`; reuse their analogies verbatim
across decks.

**Project** (Session 1, right after the context window) — the concrete, clickable instance
of the app layer, and the middle rung between a disposable prompt and a Cowork Skill: a
saved workspace (ChatGPT / Claude / Gemini) holding **standing instructions + uploaded
files**, re-sent on every chat inside it. It is the one takeaway that needs **no install**,
so it lands even for learners who never set up Cowork. It also pre-frames two later
concepts — Project folder → **working directory**, standing instructions → **Skill**.

**Agent-stack vocabulary** (the four-deck Cowork module) — taught with the analogy first, the
term as a label: **working directory** (the real folder Cowork points at = the office),
**Skill** (a book in the office library — pulled and opened only when the task calls for
it), **`/schedule`** (a standing appointment; industry term **Cron**), **Connector / MCP**
(giving the agent keys to email/calendar/drive). A **script** is "saved, repeatable
steps" — instructions the *agent* writes and runs as real code for exact, repeatable
work; you never write (or see) code. A Skill is instructions the agent *reads and
follows*; a script is code it *runs to compute*. A **Template** is a real file on the
learner's machine — their **PowerPoint template** (`.pptx`) or spreadsheet — the on-brand
layout the script *fills*; the worked example is notes → an editable `.pptx`, never a
revealjs/Quarto deck (that's authoring jargon this audience never sees). The per-workshop
deck trigger is the `deck_trigger` var, not hardcoded in the template.
The keystone framing is **composition**: a Skill bundles a script + a
template behind one trigger, and **Schedule / Connectors just run a Skill** (on a clock, or
with keys) — they're not new kinds of thing.

**RICE Pattern** (introduced in Session 1, Delegating to AI) — the delegation pattern:
- **R**ole: Who should the AI be?
- **I**nstructions: What exactly should it do? (includes format, length, tone rules)
- **C**ontext: What information should it have? (the same "context" defined in Session 1)
- **E**xamples: A sample of the desired output (few-shot prompting)

**Advanced moves** (folded into Session 1) — taught in plain language, with the industry
term kept as a label so learners recognize it: **think step by step** (Chain of Thought),
**debate it out** (Tree of Thoughts), **double-check** (Self-Consistency). Lead with the
plain-language move, not the jargon.

- **Two safety rules** — **Newspaper Test** (guards what you *paste in*; sanitize first) and,
  once agents can act, **Blast Radius / Human-in-the-Loop** (guards what the agent *does*;
  start every Skill / scheduled job / connector in draft / notify-me mode before
  act-on-its-own). All hands-on agent work runs on **copies in a staging folder**.

## Content Authoring Guidelines

When generating or modifying course content:
- Use management-friendly analogies; avoid technical jargon without explanation.
- Follow the "Explain → Demonstrate → Practice → Apply" cycle.
- Prefer a mental model plus *when/how to use it* over frameworks, ladders, and matrices.
- Cut taglines, slogans, imagined-quote bubbles, and any sentence that only restates the
  box above it. One concept box and one concrete example per slide.
- Every concept deck ends in a knowledge check; decks 4–6 also end in a follow-along.
- Use the "I like, I wish, I wonder" feedback framework.
- Support dual-language (English + Arabic key terms).

### Slide voice and density

These are acceptance criteria for any slide you write or edit, in **both** language trees.
The Arabic-specific wording contract is `notes/arabic-voice-style-guide.md`, whose §3 now
carries the same density rules.

**Density**
1. Max **~40 words of prose per slide**. Quoted prompts, the recipe card, the RICE specimen
   prompt, and the run-of-show table are *reference artifacts, not prose*: they are exempt
   and stay verbatim. Cut the explanation wrapped around them instead.
2. Max **two content blocks** per slide (a card plus one list or one line). Not card +
   paragraph + list + centered restatement + callout.
3. Bullets are **fragments, not sentences**: ≤8 words, no semicolons, no gloss clause.
4. **Delete any centered closer that only restates the card above it.**
5. **No inline `font-size:` shrink hacks.** A shrink means the slide is too full; cut text
   until the theme's type scale fits. `_quarto.yml` sets `scrollable: false`, so overflow
   is clipped silently, never scrolled.
6. **Cut before splitting.** Split a slide only when the idea needs two beats, and give the
   new slide the same `data-id` so `auto-animate` still pairs.

**Voice**
7. **No em-dash (`—`) as a connective, anywhere, in either language**, and never in a slide
   title. It was this repo's default connective and read as machine-written. Use a full
   stop, or a colon when the label is real.
8. Retire the `**Bold term** — gloss` list template. No two lists in a deck share the same
   grammar.
9. At most **one antithesis per deck** ("not X, but Y"), only where the contrast is the
   teaching point. No "Picture an…", no "Think of it as…", no `*(industry term: X)*`
   parenthetical (name the term once in the body instead).
10. Slide titles are plain statements in sentence case. No chiasmus, no two-sentence
    imperatives, no tagline that repeats the title. Section dividers (`#`) keep title case.
11. **Teach each idea once.** The two safety rules are stated in full in `overview` and
    `cowork_intro`; everywhere else they are referenced by name, not restated.

Prefer the existing SCSS vocabulary over new inline styles: `.card` + `.accent-teal|purple|
orange|navy|yellow`, `.card-dark`, `.fill-*`, `.center`, `.tight`, `.muted`, `.pill`,
`.qbox`. These use `border-inline-start` and mirror correctly under RTL; hardcoded
`border-left` / `text-align: left` do not.

**Parity:** the two template trees must keep **identical heading counts per file**. Verify
with `grep -c '^#'` on the matching pair after any structural change.

## Course Schedule Reference (KSU, ≈235 min)

Canonical order lives in `templates/workshop/index.qmd` (run-of-show) and
`examples/ksu/outline.md`. Deck slugs are descriptive and numberless. The work-mode module
is **three teaching decks plus the recipe** — one concept each, each of the three ending in
a knowledge check *and* a follow-along.

1. **Overview** (`overview.qmd`) — welcome + agenda + the two safety rules (10 min)
2. **How AI Works & Writing Great Prompts** (`how_ai_works_and_rice.qmd`) — Two Layers +
   context + **Project** + RICE + advanced moves (think step by step / debate it out /
   double-check) + Newspaper Test (45 min)
3. **Practice — Delegate a Real Task** (`practice_foundations.qmd`) — RICE on a real task,
   then save it into a Project; ends with the 10-min break (30 + 10 min)
4. **From Chat to Work Mode** (`cowork_intro.qmd`) — the keystone of the module: asking
   *about* the work vs. handing *over* the work; working directory = office; the second
   safety rule (undo test / blast radius); staging copies; instructor demo + follow-along (25 min)
5. **Build It Once** (`skills_scripts_templates.qmd`) — Skill (book) → Script (exact
   numbers) → Template (the layout) → composition. **Demo, not a build block**; ends in a
   follow-along where learners paste a provided Skill and run it (20 min)
6. **How Far This Goes** (`how_far_this_goes.qmd`) — Schedule **and** Connectors merged:
   both just *run a Skill*, on a clock or with keys; wider blast radius; module key
   takeaways (15 min)
7. **Your Recipe** (`recipe.qmd`) — the one-page take-home: three prompts they already
   watched work, to run on their own files; both safety rules; pick which to run first (10 min)
8. **Grounding & Creating with NotebookLM** (`notebooklm_grounding_and_slides.qmd`) —
   grounding + citations + slide creation (40 min)
9. **Your AI Assistant** (`wrap_up.qmd`) — recap + name one recurring task to try first +
   safety (30 min)

### Online delivery: follow-alongs, not practice blocks

The workshop is delivered **online**, where an open practice block is the thing learners
opt out of. So the doing is dissolved into the flow: decks 4–6 each end in a **3-minute
follow-along** (`followalong_*` fragments) — a **provided prompt on a provided file**, run
by everyone at once, with exactly one obvious outcome. The rule: **if it can fail live, it
isn't a follow-along.** The instructor demo (`handover_demo`) must be *replicable* — the
exact prompt appears on screen and in the recipe. Real practice happens async from
`recipe_card`; setup (app install + staging folder) is **pre-work**, not session time.

The delivery loop is therefore **Show → Mirror → Take home**, not Show → Build → Refine.
