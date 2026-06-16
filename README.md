# AI at Work: Build the Workflows That Win Back Your Week

This repository hosts the **AI at Work** workshops — hands-on programs that teach managers,
professionals, and faculty to turn the work they repeat into reusable, measurable AI
workflows, run by an AI agent that works as a permanent member of their team. Each workshop
is a self-contained top-level folder; the root [`index.qmd`](index.qmd) is the portal.

| Workshop | Folder | Outline |
|---|---|---|
| Hermes Agent Course (3-day / 12 sessions) | `hermes-agent-course/` | [outline](hermes-agent-course/outline.md) |
| Building Your Own AI Assistant (KSU, half-day) | `ksu-workshop/` | [outline](ksu-workshop/outline.md) |

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
quarto render hermes-agent-course/slides/session_1_mindset_and_automation_backlog.qmd
quarto preview hermes-agent-course/slides/session_1_mindset_and_automation_backlog.qmd
```

## Project Structure

- **`index.qmd`**: Root portal page linking the workshops (URLs mirror the folder paths — keep them stable).
- **`_quarto.yml`** / **`slides_template/assets/`**: Root Quarto config and SDAIA brand assets (theme, logos, fonts) applied globally to every deck.
- **`hermes-agent-course/`**: The 3-day / 11-session Hermes course — `index.qmd`, `outline.md`, `slides/`, `data/`, `reference/`.
- **`ksu-workshop/`**: The standalone KSU half-day workshop — `index.qmd`, `outline.md`, `slides/`, `data/`.
- **`prompts/`**: Prompt guides and instructor templates.
- **`notes/`**: Loose planning notes, idea lists, and drafts.
