# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Layout

This repo hosts **multiple SDAIA workshops**, each a self-contained top-level folder with
its own `index.qmd`, `outline.md`, `slides/`, and `data/`. A root `index.qmd` is the
**portal** that links the offerings (URLs mirror these folder paths, so keep them stable):

- `hermes-agent-course/` — the 3-day / 11-session Hermes course (the program described below). *Listed under "Project Overview".*
- `ksu-workshop/` — a standalone half-day workshop for KSU faculty (Claude Cowork; portable concepts).
- `employee-ai-workshop/` — a 3-day "AI Productivity at Work" workshop for general employees (Claude Cowork as the demo tool, taught portably; generic-office examples). Reuses the shared `chunks/` Foundation and adds one own deck: `tools_landscape.qmd` — a short Day-3 "Pick Your AI & Expand Your Toolkit" brief (chat vs. agent + ChatGPT/Claude/Gemini + Cowork/Antigravity/Hermes + curated AI-tools survey + optional local-LLM awareness) that ends in a hands-on "try one tool". Chat-vs-agent is also taught on Day 2 in `meet_cowork.qmd`.
- `chunks/` — shared **concept-only slide chunks** (`chunks/_*.qmd`), single-sourced and reused across workshops, plus `chunks/reference/` (the plain-language concept definitions). This is the **Foundation** material; it is a *library*, not a course — there is no `foundation/` unit.
- `slides_template/`, `_quarto.yml` — shared SDAIA branding + Quarto config at the repo root, applied globally to every deck.
- `prompts/`, `notes/` — shared prompt guides/templates and loose planning notes.

> The Hermes course is in progress and currently **hidden** from the root portal `index.qmd`
> (commented placeholder); the KSU and Employee workshops are the listed offerings.

### Shared chunks (the Foundation)

The Day-1 / foundation concepts (Two Layers, context, context window, script, RICE,
advanced moves, Newspaper Test, grounding) live **once** in `chunks/_*.qmd` and are pulled
into each workshop's decks with `{{< include ../../chunks/_two_layers.qmd >}}` (path is
relative to the including deck — two levels up from a workshop's `slides/`). **Rules:**
chunks are **concept-only** (no worked examples — each workshop adds its own example slides
around the include); they carry **no front matter** and start at a slide boundary (`#`/`##`);
and they must **not** contain a literal `{{< include … >}}` in comments (Quarto processes
shortcodes inside HTML comments → self-include recursion). `chunks/_preview.qmd` renders all
chunks together for branding/overflow checks. Leading-underscore files are auto-ignored by
Quarto, so chunks never render as standalone decks.

## Project Overview

**AI at Work: Build the Workflows That Win Back Your Week** — a 3-day, 11-session
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

**The running spine:** In the Day-1 **kickoff** each participant writes an **Automation
Backlog** (their recurring tasks) and starts a **Time Log**. Every build session pulls one
task from that backlog, builds a workflow for it, and records before/after time; Session 11
(the finale) totals it into **hours won back per week** (the ROI capstone). The worksheet
lives at `prompts/automation_backlog_and_time_log.md`.

> Note: `hermes-agent-course/outline.md` and the concepts reference are the source of truth.
> The course is structured as a **Foundation** block (Day 1, composed from the shared
> `chunks/` library + manager examples) and an **Expansion** block (Days 2–3, where each
> session builds on a Foundation artifact). Decks are named with **descriptive, numberless
> slugs** (e.g. `two_layers.qmd`, `skills.qmd`, `roi_finale.qmd`) — session order lives in
> `outline.md` and `index.qmd`, not in filenames. Keep decks aligned with the outline if it changes.

### Key Files (Hermes course)
- `hermes-agent-course/outline.md` — master course outline (Foundation + Expansion, schedule, activities). Primary doc.
- `chunks/reference/mental_model_and_agent_concepts.md` — canonical plain-language
  definitions (two layers, context, script, Project, `CLAUDE.md`, Skill, Memory, Cron,
  Connector, blast radius). **Shared** source of truth behind the foundation chunks.
- `hermes-agent-course/slides/*.qmd` — the SDAIA-branded Quarto reveal.js decks (Day-1 decks `{{< include >}}` the shared chunks; Day-2/3 are the expansion sessions).
- `hermes-agent-course/slides/_course_overview.qmd` — canonical agenda (Foundation + Expansion).
- `_quarto.yml` — Quarto project config at the **repo root** (global SDAIA branding; renders the source tree into repo-root `output/`).
- `slides_template/assets/` — SDAIA brand assets (`sdaia.scss`, logo/icon SVGs, `splash.lua`, `favicon.html`) referenced globally by `_quarto.yml`.
- `hermes-agent-course/data/` — datasets used in hands-on activities (e.g. `expenses_export.csv`).
- `prompts/` — prompt guides and instructor templates.
- `notes/` — loose planning notes, idea lists, and drafts.

## Slides

Slides are SDAIA-branded Quarto reveal.js decks. Branding is applied globally in the
root `_quarto.yml`, so each deck's front matter stays minimal
(`title` / `subtitle` / `date` / `format: revealjs`). Author, render, preview,
screenshot, and visually verify them with the **`author-verify-slides`** skill —
branding and Quarto patterns are constant across SDAIA slide projects.

**Run all commands from the repo root** (Quarto finds `_quarto.yml` there and mirrors
the source path into `output/`, e.g. `hermes-agent-course/slides/foo.qmd` →
`output/hermes-agent-course/slides/foo.html`):

- Render one deck: `quarto render hermes-agent-course/slides/<deck>.qmd`
- Render all decks: `quarto render`
- Preview with live reload: `quarto preview hermes-agent-course/slides/<deck>.qmd`
- Render + screenshot + verify branding/overflow:
  `python .claude/skills/author-verify-slides/driver.py hermes-agent-course/slides/<deck>.qmd --all --reveal-all`

`output/` is gitignored.

## Core Teaching Framework

**The Two Layers** (the keystone, introduced in Session 1) — the mental model everything
else hangs off. The **model layer** is a "brain in a jar": stateless, knows nothing about
you, just predicts the next word, forgets everything when a request ends. The **app layer**
is the "office around the brain": it stores your info in a directory and **re-sends the
relevant context on every request**. Once learners see this, `CLAUDE.md`, Projects, Memory,
and Skills stop being magic — they're all the app getting smarter about *what to re-send*.
Full definitions live in `chunks/reference/mental_model_and_agent_concepts.md`;
reuse its analogies verbatim across decks (they are already single-sourced in `chunks/_two_layers.qmd`).

**Agent-stack vocabulary** (Day 2–3) — taught with the analogy first, the term as a label:
**Project** (a dedicated office/folder), **`CLAUDE.md` / `AGENTS.md`** (standing
instructions pinned to the wall — two filenames, one idea), **Skill** (a book in the
office library — pulled and opened only when the task calls for it), **Memory** (the
agent's notebook about you), **Cron** (a standing appointment), **Connector / MCP**
(giving the agent keys to email/calendar/drive). A **script** is "saved, repeatable
steps" — instructions the *agent* writes and runs as real code for exact, repeatable
work; you never write (or see) code. A Skill is instructions the agent *reads and
follows*; a script is code it *runs to compute*.

**RICE Pattern** (introduced in Session 2, Delegating to AI) — the delegation pattern:
- **R**ole: Who should the AI be?
- **I**nstructions: What exactly should it do? (includes format, length, tone rules)
- **C**ontext: What information should it have? (the same "context" defined in Session 1)
- **E**xamples: A sample of the desired output (few-shot prompting)

**Advanced moves** (folded into Session 2) — taught in plain language, with the industry
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

**Day 1 — Foundations: Think Like an AI-Native (Kickoff + Sessions 1–3)**
- *Kickoff.* Welcome & Your Automation Backlog (the running spine + bottleneck test)
1. How AI Actually Works — The Two Layers (model vs app layer, context, script)
2. Delegating to AI — The RICE Pattern + advanced moves (think step by step / debate it out / double-check); also hosts the Newspaper Test + Safe/Risky micro-check
3. Grounding AI in Truth — The Research Workflow

**Day 2 — Meet Your Agent: Build Your Hermes Operations Team (Sessions 4–7)**
4. Meet Hermes — Setup & Your First Agent Run (agent-era safety: blast radius / human-in-the-loop)
5. Projects & Standing Instructions — `CLAUDE.md` / `AGENTS.md`
6. Skills — Your Reusable Workflow Library
7. Memory — Teaching the Agent to Remember You

**Day 3 — Agents That Act: Executive Output & ROI (Sessions 8–11)**
8. Cron & Connectors — The Agent That Acts on Its Own
9. From Notes to Narrative — The Amazon Method + Design Engine
10. Interviewing Your Data
11. The ROI Finale + Your Workflow Library
