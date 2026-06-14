# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**AI at Work: Build the Workflows That Win Back Your Week** — a 3-day, 12-session
instructor-led workshop teaching managers and professionals to use AI as a permanent
member of their operations team (not as a search engine). The deliverable is a set of
reusable AI workflows for business process automation, framed around **AI productivity**
and **measurable time won back**.

**Primary stack:** The hands-on tool is the **Hermes desktop agent** (Projects,
`CLAUDE.md`/`AGENTS.md`, Skills, Memory, Cron, Connectors). Concepts stay **portable** —
each feature is taught as *the general idea → how Hermes does it → what other apps
(ChatGPT, Gemini, Claude, Coworker) call it*. The audience is non-technical, so the agent
is demystified, not assumed: **nobody writes code.**

The delivery loop is **Show** (instructor demo) → **Build** (students apply a workflow
to a real task) → **Refine** (group critique).

**The running spine:** In Session 1 each participant writes an **Automation Backlog**
(their recurring tasks) and starts a **Time Log**. Every build session pulls one task
from that backlog, builds a workflow for it, and records before/after time; Session 12
totals it into **hours won back per week** (the ROI capstone). The worksheet lives at
`prompts/automation_backlog_and_time_log.md`.

> Note: `outline.md` and the concepts reference are the current source of truth. The
> `.qmd` slide decks have **not** yet been re-authored for the 3-day/Hermes redesign —
> the existing decks under `course_content/slides/` reflect the older 2-day structure.

### Key Files
- `outline.md` — master course outline (12 sessions, schedule, activities). Primary doc.
- `course_content/reference/mental_model_and_agent_concepts.md` — canonical plain-language
  definitions (two layers, context, script, Project, `CLAUDE.md`, Skill, Memory, Cron,
  Connector, blast radius). Source of truth for the Session 2 + Day-2 slide decks.
- `course_content/slides/*.qmd` — the SDAIA-branded Quarto reveal.js slide decks (one per session).
- `course_content/slides/_course_overview.qmd` — canonical session list / agenda.
- `_quarto.yml` — Quarto project config at the **repo root** (global SDAIA branding; renders the source tree into repo-root `output/`).
- `slides_template/assets/` — SDAIA brand assets (`sdaia.scss`, logo/icon SVGs, `splash.lua`, `favicon.html`) referenced globally by `_quarto.yml`.
- `course_content/data/` — datasets used in hands-on activities (e.g. `expenses_export.csv`).
- `prompts/` — prompt guides and instructor templates.
- `notes/` — loose planning notes, idea lists, and drafts.

## Slides

Slides are SDAIA-branded Quarto reveal.js decks. Branding is applied globally in the
root `_quarto.yml`, so each deck's front matter stays minimal
(`title` / `subtitle` / `date` / `format: revealjs`). Author, render, preview,
screenshot, and visually verify them with the **`author-verify-slides`** skill —
branding and Quarto patterns are constant across SDAIA slide projects.

**Run all commands from the repo root** (Quarto finds `_quarto.yml` there and mirrors
the source path into `output/`, e.g. `course_content/slides/foo.qmd` →
`output/course_content/slides/foo.html`):

- Render one deck: `quarto render course_content/slides/<deck>.qmd`
- Render all decks: `quarto render`
- Preview with live reload: `quarto preview course_content/slides/<deck>.qmd`
- Render + screenshot + verify branding/overflow:
  `python .claude/skills/author-verify-slides/driver.py course_content/slides/<deck>.qmd --all --reveal-all`

`output/` is gitignored.

## Core Teaching Framework

**The Two Layers** (the keystone, introduced in Session 2) — the mental model everything
else hangs off. The **model layer** is a "brain in a jar": stateless, knows nothing about
you, just predicts the next word, forgets everything when a request ends. The **app layer**
is the "office around the brain": it stores your info in a directory and **re-sends the
relevant context on every request**. Once learners see this, `CLAUDE.md`, Projects, Memory,
and Skills stop being magic — they're all the app getting smarter about *what to re-send*.
Full definitions live in `course_content/reference/mental_model_and_agent_concepts.md`;
reuse its analogies verbatim across decks.

**Agent-stack vocabulary** (Day 2–3) — taught with the analogy first, the term as a label:
**Project** (a dedicated office/folder), **`CLAUDE.md` / `AGENTS.md`** (standing
instructions pinned to the wall — two filenames, one idea), **Skill** (a saved recipe
card), **Memory** (the agent's notebook about you), **Cron** (a standing appointment),
**Connector / MCP** (giving the agent keys to email/calendar/drive). A **script** is just
"saved, repeatable steps" — plain language, never code.

**RICE Pattern** (introduced in Session 3, Delegating to AI) — the delegation pattern:
- **R**ole: Who should the AI be?
- **I**nstructions: What exactly should it do? (includes format, length, tone rules)
- **C**ontext: What information should it have? (the same "context" defined in Session 2)
- **E**xamples: A sample of the desired output (few-shot prompting)

**Advanced moves** (folded into Session 3) — taught in plain language, with the industry
term kept as a label so learners recognize it: **think step by step** (Chain of Thought),
**debate it out** (Tree of Thoughts), **double-check** (Self-Consistency). Lead with the
plain-language move, not the jargon.

**Two safety rules** — **Newspaper Test** (guards what you *paste in*; sanitize first) and,
once agents can act, **Blast Radius / Human-in-the-Loop** (guards what the agent *does*;
start every Skill/Cron/Connector in draft / notify-me mode before act-on-its-own). All
hands-on agent work runs in a **sandbox folder with dummy data**.

## Content Authoring Guidelines

When generating or modifying course content:
- Use management-friendly analogies; avoid technical jargon without explanation.
- Follow the "Explain → Demonstrate → Practice → Apply" cycle.
- Maintain ~70% hands-on building time, ~30% theory.
- Use the "I like, I wish, I wonder" feedback framework.
- Support dual-language (English + Arabic key terms).

## Course Schedule Reference

**Day 1 — Foundations: Think Like an AI-Native (Sessions 1–4)**
1. The AI-Native Mindset & Your Automation Backlog
2. How AI Actually Works — The Two Layers (model vs app layer, context, script)
3. Delegating to AI — The RICE Pattern + advanced moves (think step by step / debate it out / double-check)
4. Grounding AI in Truth — The Research Workflow

**Day 2 — Meet Your Agent: Build Your Hermes Operations Team (Sessions 5–8)**
5. Meet Hermes — Setup & Your First Agent Run (agent-era safety: blast radius / human-in-the-loop)
6. Projects & Standing Instructions — `CLAUDE.md` / `AGENTS.md`
7. Skills — Your Reusable Workflow Library
8. Memory — Teaching the Agent to Remember You

**Day 3 — Agents That Act: Executive Output & ROI (Sessions 9–12)**
9. Cron & Connectors — The Agent That Acts on Its Own
10. From Notes to Narrative — The Amazon Method + Design Engine
11. Interviewing Your Data
12. The ROI Finale + Your Workflow Library
