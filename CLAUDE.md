# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**AI at Work: Build the Workflows That Win Back Your Week** — a 2-day, 10-session
instructor-led workshop teaching managers and professionals to use AI as a permanent
member of their operations team (not as a search engine). The deliverable is a set of
reusable AI workflows for business process automation, framed around **AI productivity**
and **measurable time won back**.

The delivery loop is **Show** (instructor demo) → **Build** (students apply a workflow
to a real task) → **Refine** (group critique).

**The running spine:** In Session 1 each participant writes an **Automation Backlog**
(their recurring tasks) and starts a **Time Log**. Every build session pulls one task
from that backlog, builds a workflow for it, and records before/after time; Session 10
totals it into **hours won back per week** (the ROI capstone). The worksheet lives at
`prompts/automation_backlog_and_time_log.md`.

> Note: Sessions 7–10 are described in `outline.md` but their slide decks are not yet
> authored — only Sessions 1–6 have `.qmd` files.

### Key Files
- `outline.md` — master course outline (10 sessions, schedule, activities). Primary doc.
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

**RICE Pattern** (introduced in Session 2, Delegating to AI) — the delegation pattern:
- **R**ole: Who should the AI be?
- **I**nstructions: What exactly should it do? (includes format, length, tone rules)
- **C**ontext: What information should it have?
- **E**xamples: A sample of the desired output (few-shot prompting)

**Solving Hard Problems** (Session 5) — taught in plain language, with the industry term
kept as a label so learners recognize it: **think step by step** (Chain of Thought),
**debate it out** (Tree of Thoughts), **double-check** (Self-Consistency). Lead with the
plain-language move, not the jargon.

## Content Authoring Guidelines

When generating or modifying course content:
- Use management-friendly analogies; avoid technical jargon without explanation.
- Follow the "Explain → Demonstrate → Practice → Apply" cycle.
- Maintain ~70% hands-on building time, ~30% theory.
- Use the "I like, I wish, I wonder" feedback framework.
- Support dual-language (English + Arabic key terms).

## Course Schedule Reference

**Day 1 — Build Your First Workflows (Sessions 1–5)**
1. The AI-Native Mindset & Your Automation Backlog
2. Delegating to AI — The RICE Pattern
3. Reusable Workflows — Building Specialized Assistants
4. Grounding AI in Truth — The Research Workflow
5. Solving Hard Problems (think step by step / debate it out / double-check)

**Day 2 — Executive Output & Personal Systems (Sessions 6–10)**
6. From Notes to Narrative (The Amazon Method)
7. The Design Engine
8. Interviewing Your Data
9. Your Personal AI System
10. The ROI Finale
