# Prompt Engineering 2 Days Course

This repository contains the course materials and slide decks for the Prompt Engineering course.

> [!NOTE]
> Please refer to [outline.md](outline.md) for the detailed course outline, schedule, and session descriptions.

## Rendering Slides

This project uses [Quarto](https://quarto.org/) for slide generation. The Quarto
project lives in `course_content/slides/`, so run the commands from there.

To render the slides, run:

```bash
cd course_content/slides
quarto render
```

To preview the slides locally with live reload:

```bash
cd course_content/slides
quarto preview
```

## Project Structure

- **`course_content/slides/`**: The Quarto (`.qmd`) reveal.js slide decks — one per session. Render from here.
- **`course_content/data/`**: Datasets used in the hands-on activities.
- **`prompts/`**: Prompt guides and instructor templates.
- **`notes/`**: Loose planning notes, idea lists, and drafts.
- **`outline.md`**: The master outline for the course.
