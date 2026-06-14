# Prompt Engineering 2 Days Course

This repository contains the course materials and slide decks for the Prompt Engineering course.

> [!NOTE]
> Please refer to [outline.md](outline.md) for the detailed course outline, schedule, and session descriptions.

## Rendering Slides

This project uses [Quarto](https://quarto.org/) for slide generation. The Quarto
project config (`_quarto.yml`) lives at the **repo root** and applies SDAIA branding
globally, so run all commands from the repo root. Rendered HTML is written to a
repo-root `output/` directory (gitignored), mirroring the source path.

To render all slide decks, run:

```bash
quarto render
```

To render or preview a single deck with live reload:

```bash
quarto render course_content/slides/session_1_ai_native_mindset.qmd
quarto preview course_content/slides/session_1_ai_native_mindset.qmd
```

## Project Structure

- **`_quarto.yml`** / **`slides_template/assets/`**: Root Quarto config and SDAIA brand assets (theme, logos, fonts) applied globally to every deck.
- **`course_content/slides/`**: The Quarto (`.qmd`) reveal.js slide decks — one per session.
- **`course_content/data/`**: Datasets used in the hands-on activities.
- **`prompts/`**: Prompt guides and instructor templates.
- **`notes/`**: Loose planning notes, idea lists, and drafts.
- **`outline.md`**: The master outline for the course.
