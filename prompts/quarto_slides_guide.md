---
name: quarto-revealjs
description: Create professional reveal.js presentations using Quarto. Use when the user requests to make slides, presentations, or slide decks using Quarto, or mentions reveal.js presentations. Covers slide creation, themes, backgrounds, code blocks, incremental lists, layouts, and all Quarto reveal.js features.
---

# Quarto Reveal.js Presentations

## Overview

Quarto creates reveal.js presentations from markdown files using the `.qmd` extension. Render with `quarto render` or preview with `quarto preview`.

## Basic Structure

### Minimal Presentation

```yaml
---
title: "Presentation Title"
author: "Author Name"
format: revealjs
---

## First Slide

- Bullet point one
- Bullet point two

## Second Slide

Content here
```

### Creating Slides

- **Level 2 headings (`##`)** → new slides
- **Level 1 headings (`#`)** → section dividers with title slides
- **Horizontal rules (`---`)** → slides without titles

### Title Slide

Omit `title` and `author` from YAML to skip automatic title slide.

## Essential Features

### Incremental Lists

**Global:**
```yaml
format:
  revealjs:
    incremental: true
```

**Per-list:**
```markdown
::: {.incremental}
- Item appears first
- Then this item
:::

::: {.nonincremental}
- All items at once
:::
```

**Pauses:**
```markdown
Content before

. . .

Content after (hidden until advanced)
```

### Multiple Columns

```markdown
:::: {.columns}
::: {.column width="40%"}
Left column
:::
::: {.column width="60%"}
Right column
:::
::::
```

### Content Overflow

```markdown
## Slide {.smaller}    # Smaller font
## Slide {.scrollable} # Enable scrolling
```

Or globally:
```yaml
format:
  revealjs:
    smaller: true
    scrollable: true
```

### Speaker Notes

```markdown
## Slide Title

::: {.notes}
Speaker notes (press 'S' to view)
:::
```

## Themes & Styling

### Themes

Available: `beige`, `blood`, `dark`, `default`, `dracula`, `league`, `moon`, `night`, `serif`, `simple`, `sky`, `solarized`

```yaml
format:
  revealjs:
    theme: dark
```

### Footer & Logo

```yaml
format:
  revealjs:
    logo: logo.png
    footer: "Footer text"
```

Remove per-slide: `## Title {footer=false}`

## Code

### Basic Display

````markdown
```{.python}
import numpy as np
```
````

### Line Highlighting

````markdown
```{.python code-line-numbers="6-8"}
# Lines 6-8 highlighted
```

```{.python code-line-numbers="|6|9"}
# Progressive: all → line 6 → line 9
```
````

### Executable Code

**Important:** Code does NOT echo by default in presentations.

````markdown
```{python}
#| echo: true
#| output-location: fragment  # Options: fragment, slide, column, column-fragment

import matplotlib.pyplot as plt
# code
```
````

## Backgrounds

### Color & Gradients

```markdown
## Title {background-color="aquamarine"}

## Title {background-gradient="linear-gradient(to bottom, #283b95, #17b2c3)"}
```

### Images & Video

```markdown
## Title {background-image="image.jpg" background-opacity="0.5"}

## Title {background-video="video.mp4" background-video-loop="true"}
```

### Title Slide Background

```yaml
---
title: My Presentation
format: revealjs
title-slide-attributes:
  data-background-image: image.png
  data-background-size: contain
  data-background-opacity: "0.5"
---
```

## Rendering

```bash
quarto render presentation.qmd    # Render to HTML
quarto preview presentation.qmd   # Live preview
```

## Quick Template

```markdown
---
title: "Project Update"
author: "Your Name"
format:
  revealjs:
    theme: dark
    incremental: true
    footer: "Confidential"
---

## Overview

- Point one
- Point two

## Details {.smaller}

Detailed content

## Code {.scrollable}

```{python}
#| echo: true
import pandas as pd
data = pd.read_csv("data.csv")
```

## Questions? {background-color="#283b95"}
```
