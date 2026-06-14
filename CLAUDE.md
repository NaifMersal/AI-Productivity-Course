# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**The AI-Native Professional: Building Your Digital Factory** — a 2-day, 10-session
instructor-led workshop teaching managers and professionals to use AI as a permanent
member of their operations team (not as a search engine). The deliverable is a set of
reusable AI workflows for business process automation.

The delivery loop is **Show** (instructor demo) → **Build** (students apply the
framework to a project) → **Refine** (group critique).

### Key Files
- `outline.md` — master course outline (10 sessions, schedule, activities). Primary doc.
- `course_content/slides/*.qmd` — the SDAIA-branded Quarto reveal.js slide decks (one per session).
- `course_content/slides/_course_overview.qmd` — canonical session list / agenda.
- `course_content/slides/_quarto.yml` — Quarto project config (renders `*.qmd` to `output/`).
- `course_content/data/` — datasets used in hands-on activities (e.g. `expenses_export.csv`).
- `prompts/` — prompt guides and instructor templates.
- `notes/` — loose planning notes, idea lists, and drafts.

## Slides

Slides are SDAIA-branded Quarto reveal.js decks. Author, render, preview, screenshot,
and visually verify them with the **`author-verify-slides`** skill — branding and Quarto
patterns are constant across SDAIA slide projects.

- Render: `quarto render` (run from `course_content/slides/`; outputs to `output/`, gitignored).
- Preview with live reload: `quarto preview`.

## Core Teaching Framework

**R-C-T-C Pattern** (introduced in Session 2, The Science of Delegation):
- **R**ole: Who should the AI be?
- **C**ontext: What information should it have?
- **T**ask: What exactly should it do?
- **C**onstraint: What are the limitations/rules?

**Advanced Techniques** (Session 5): Chain of Thought (CoT), Tree of Thoughts (ToT),
Self-Consistency.

## Content Authoring Guidelines

When generating or modifying course content:
- Use management-friendly analogies; avoid technical jargon without explanation.
- Follow the "Explain → Demonstrate → Practice → Apply" cycle.
- Maintain ~70% hands-on building time, ~30% theory.
- Use the "I like, I wish, I wonder" feedback framework.
- Support dual-language (English + Arabic key terms).

## Course Schedule Reference

**Day 1 — Architecting the Brain (Sessions 1–5)**
1. The AI-Native Mindset
2. The Science of Delegation (R-C-T-C)
3. Building "Specialized Brains" (Context)
4. The First Interaction — The Research Stack
5. Advanced Prompt Engineering (CoT, ToT, Self-Consistency)

**Day 2 — Advanced Intelligence & Executive Output (Sessions 6–10)**
6. The Narrative Architect (The Amazon Method)
7. The Design Engine
8. Interviewing Your Data
9. Personal Productivity Systems
10. The Finale & ROI
