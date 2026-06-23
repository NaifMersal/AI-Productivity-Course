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
- `chunks/reference/` — the canonical plain-language concept definitions (the shared source
  behind the inline concept slides). Documentation only; not rendered.
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

The foundation concepts (Two Layers, context, context window, script, RICE, advanced moves,
Newspaper Test, grounding, **Connectors/MCP**) are authored **inline in the template decks**
under `templates/workshop/slides/`. Since `build.py` renders the same templates for every
workshop, editing a concept once updates every workshop — keep concept edits in the
templates, never in a generated `<id>-workshop/` copy. The canonical plain-language wording
behind these slides lives in `chunks/reference/`; keep the slides consistent with it. The
**per-workshop** material (worked examples, sample prompts, demos) is the only thing that
varies, and it lives in `examples/<id>/fragments/` (pulled in via `<!-- EXAMPLE: key -->`)
plus the `vars` strings in `config/workshops.json`.

## Project Overview

**Building Your Own AI Assistant** — a half-day (~4.5 hr), hands-on workshop teaching **KSU
faculty** to use AI as a permanent member of their team (not as a search engine). By the
end each participant has a working **AI assistant they set up themselves** plus 2–3
automations on their own academic work, framed around **measurable time won back**.

**Hands-on tool:** **Claude Cowork** (Anthropic's desktop agent) — chosen because it is the
fastest to set up. Concepts stay **portable** (ChatGPT, Gemini, Claude, NotebookLM named as
alternatives). The audience is non-technical: **nobody writes code.**

The delivery loop is **Show** (instructor demo) → **Build** (faculty apply a workflow to a
real task) → **Refine** (group critique), ~70% hands-on. All hands-on agent work runs in a
**sandbox folder with dummy data**.

### Key Files
- `examples/ksu/outline.md` — the KSU workshop outline (sessions, schedule, activities). Primary doc.
- `chunks/reference/mental_model_and_agent_concepts.md` — canonical plain-language
  definitions (two layers, context, script, Skill, Schedule/Cron, Connector/MCP, blast
  radius). **Shared** source of truth behind the inline concept slides.
- `templates/workshop/slides/*.qmd` — the structural SDAIA-branded reveal.js decks, with the
  concept slides authored inline.
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
Full definitions live in `chunks/reference/mental_model_and_agent_concepts.md`; reuse its
analogies verbatim across decks (the Two Layers concept slides live inline in
`templates/workshop/slides/how_ai_works_and_rice.qmd`).

**Agent-stack vocabulary** (the four-deck Cowork module) — taught with the analogy first, the
term as a label: **working directory** (the real folder Cowork points at = the office),
**Skill** (a book in the office library — pulled and opened only when the task calls for
it), **`/schedule`** (a standing appointment; industry term **Cron**), **Connector / MCP**
(giving the agent keys to email/calendar/drive). A **script** is "saved, repeatable
steps" — instructions the *agent* writes and runs as real code for exact, repeatable
work; you never write (or see) code. A Skill is instructions the agent *reads and
follows*; a script is code it *runs to compute*. A **Template** is the on-brand layout the
script *fills*. The keystone framing is **composition**: a Skill bundles a script + a
template behind one trigger, and **Schedule / Connectors just run a Skill** (on a clock, or
with keys) — they're not new kinds of thing. Keep these consistent with
`chunks/reference/mental_model_and_agent_concepts.md` (Script / Template / Composition).

**RICE Pattern** (introduced in Session 1, Delegating to AI) — the delegation pattern:
- **R**ole: Who should the AI be?
- **I**nstructions: What exactly should it do? (includes format, length, tone rules)
- **C**ontext: What information should it have? (the same "context" defined in Session 1)
- **E**xamples: A sample of the desired output (few-shot prompting)

**Advanced moves** (folded into Session 1) — taught in plain language, with the industry
term kept as a label so learners recognize it: **think step by step** (Chain of Thought),
**debate it out** (Tree of Thoughts), **double-check** (Self-Consistency). Lead with the
plain-language move, not the jargon.

**Two safety rules** — **Newspaper Test** (guards what you *paste in*; sanitize first) and,
once agents can act, **Blast Radius / Human-in-the-Loop** (guards what the agent *does*;
start every Skill / scheduled job / connector in draft / notify-me mode before
act-on-its-own). All hands-on agent work runs in a **sandbox folder with dummy data**.

## Content Authoring Guidelines

When generating or modifying course content:
- Use management-friendly analogies; avoid technical jargon without explanation.
- Follow the "Explain → Demonstrate → Practice → Apply" cycle.
- Maintain ~70% hands-on building time, ~30% theory.
- Use the "I like, I wish, I wonder" feedback framework.
- Support dual-language (English + Arabic key terms).

## Course Schedule Reference (KSU, ≈270 min)

Canonical order lives in `templates/workshop/index.qmd` (run-of-show) and
`examples/ksu/outline.md`. Deck slugs are descriptive and numberless. The Cowork module is
**four single-idea decks** (one concept each, each ending in a knowledge check) — not one
deck.

1. **Overview** (`overview.qmd`) — welcome + agenda + the two safety rules (10 min)
2. **How AI Works & Writing Great Prompts** (`how_ai_works_and_rice.qmd`) — Two Layers +
   context + RICE + advanced moves (think step by step / debate it out / double-check) +
   Newspaper Test (45 min)
3. **Practice — Delegate a Real Task** (`practice_foundations.qmd`) — RICE on a real task;
   ends with the 10-min break (25 + 10 min)
4. **From Chat to Cowork** (`cowork_intro.qmd`) — chat vs. agent, working directory =
   office, the second safety rule (undo test / blast radius) woven inline, sandbox (20 min)
5. **Build It Once: Skills, Scripts & Templates** (`skills_scripts_templates.qmd`) — the
   composition centerpiece: Skill (book) → Script (the worker it calls) → Template (the
   layout it fills) → composition (one phrase → finished on-brand result) (30 min)
6. **Schedule: Run It Without You** (`schedule.qmd`) — `/schedule` runs a Skill on a clock;
   guardrails first; starter library (15 min)
7. **Connectors: Reaching Into Other Buildings** (`connectors.qmd`) — keys to inbox /
   calendar / drive (MCP), wider blast radius, connector + skill + schedule together;
   ends with the module key takeaways (15 min)
8. **Practice — Build Your First Workflows** (`practice_automation.qmd`) — first run +
   package a Skill (30 min)
9. **Grounding & Creating with NotebookLM** (`notebooklm_grounding_and_slides.qmd`) —
   grounding + citations + slide creation (40 min)
10. **Your AI Assistant** (`wrap_up.qmd`) — recap + tally hours won back + safety (30 min)
