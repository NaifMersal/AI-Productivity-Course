---
name: quarto-revealjs
description: Create professional reveal.js presentations using Quarto. Use when the user requests slides, presentations, or slide decks.
---

# Quarto Reveal.js Presentations

Quarto creates reveal.js presentations from `.qmd` files. Render with `quarto render` or preview with `quarto preview`.

## Basic Structure

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

**Slide creation:**
- `##` (Level 2) → new slides
- `#` (Level 1) → section dividers with title slides
- `---` → slides without titles

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
Left column content
:::
::: {.column width="60%"}
Right column content
:::
::::
```

### Content Overflow

```markdown
## Slide {.smaller}    # Smaller font
## Slide {.scrollable} # Enable scrolling
```

### Speaker Notes

```markdown
## Slide Title

::: {.notes}
Speaker notes (press 'S' to view)
:::
```

## Themes & Styling

Available themes: `beige`, `blood`, `dark`, `default`, `dracula`, `league`, `moon`, `night`, `serif`, `simple`, `sky`, `solarized`

```yaml
format:
  revealjs:
    theme: dark
    logo: logo.png
    footer: "Footer text"
```

## Code Blocks

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

```markdown
```{python}
#| echo: true
#| output-location: fragment  # Options: fragment, slide, column, column-fragment

import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```
```

## Backgrounds

```markdown
## Title {background-color="#1C355E"}

## Title {background-gradient="linear-gradient(135deg, #1C355E, #00C9A7)"}

## Title {background-image="image.jpg" background-opacity="0.5"}

## Title {background-video="video.mp4" background-video-loop="true"}
```

### Title Slide Background

```yaml
title-slide-attributes:
  data-background-image: image.png
  data-background-size: contain
  data-background-opacity: "0.5"
```

## Brand Styling

### Complete YAML Configuration

```yaml
---
title: "Session Title"
subtitle: "Descriptive Subtitle"
author: "Your Organization"
date: today
format:
  revealjs:
    theme: [default, assets/sdaia.scss]
    logo: assets/logo.svg
    transition: slide
    transition-speed: default
    background-transition: fade
    footer: "Your Footer Text"
    slide-number: true
    controls: true
    controls-tutorial: true
    progress: true
    hash: true
    center-title-slide: true
    title-slide-attributes:
      data-background-image: "assets/background.svg"
      data-background-opacity: "0.15"
      data-background-size: "cover"
---
```

### Color Palette (WCAG Optimized)

| Role | Hex | Usage |
|------|-----|-------|
| Primary Dark | `#1C355E` | Dark backgrounds, headers |
| Teal Accent | `#00C9A7` | Success, highlights, CTA |
| Purple Accent | `#9B8EC0` | Secondary accent (WCAG AA on dark) |
| Coral/Warning | `#FF7A5C` | Warnings, emphasis |
| Text on Dark | `#FFFFFF` | White text for dark backgrounds |
| Light Background | `#F0F4F8` | Contrast slides, callout backgrounds |

**Accessibility notes:**
- Purple `#9B8EC0` on dark blue `#1C355E` achieves ~4.5:1 contrast (WCAG AA)
- Teal and coral brightened for projector visibility

### Custom Slide Classes

**Dark branded slides:**
```markdown
# Section Title {.sdaia-dark background-gradient="linear-gradient(135deg, #1C355E, #00C9A7)"}

## Slide Title {.sdaia-dark background-color="#1C355E"}
```

**Gradient combinations:**
```markdown
## Teal Gradient {background-gradient="linear-gradient(135deg, #1C355E, #00C9A7)"}

## Purple Gradient {background-gradient="linear-gradient(135deg, #1C355E, #9B8EC0)"}

## Coral Gradient {background-gradient="linear-gradient(135deg, #FF7A5C, #1C355E)"}
```

### Callout Styles

```markdown
::: {.callout-important}
## The Rule
Critical information that must not be ignored.
:::

::: {.callout-tip}
## Course Goal
Helpful guidance or objectives.
:::

::: {.callout-note}
## Notice
Supplementary information or observations.
:::
```

### Animation Patterns

**Auto-animate between slides:**
```markdown
## Slide One {auto-animate=true}

::: {data-id="concept"}
**Initial state.**
:::

## Slide Two {auto-animate=true}

::: {data-id="concept"}
**Initial state.** Now with more content.
:::
```

**Fragment animations:**
```markdown
::: {.fragment .fade-up}
Fades up into view
:::

::: {.fragment .fade-in}
Fades in
:::

::: {.fragment .highlight-red}
Highlights in red
:::

::: {.fragment .highlight-current-blue}
Highlights blue only when current
:::
```

**Fragments in columns:**
```markdown
:::: {.columns}
::: {.column width="50%"}
::: {.fragment .fade-in}
Left content appears first
:::
:::
::: {.column width="50%"}
::: {.fragment .fade-in}
Right content appears second
:::
:::
::::
```

### Transition Options

```markdown
## Zoom In {transition="zoom"}

## Fade Transition {transition="fade"}

## Slide Transition {transition="slide"}
```

### Styled Content Blocks

**Styled box with accent border:**
```markdown
::: {data-id="prompt" style="background: #1C355E; padding: 1.5em; border-radius: 12px; border-left: 4px solid #FF7A5C;"}
Content with coral accent border
:::
```

**Fit text to screen:**
```markdown
::: {.r-fit-text}
Large Important Text
:::
```

## Branded Quick Template

```markdown
---
title: "Presentation Title"
subtitle: "Session Description"
author: "Organization Name"
date: today
format:
  revealjs:
    theme: [default, assets/sdaia.scss]
    logo: assets/logo.svg
    transition: slide
    background-transition: fade
    footer: "Your Organization"
    slide-number: true
    controls: true
    progress: true
    center-title-slide: true
    title-slide-attributes:
      data-background-image: "assets/background.svg"
      data-background-opacity: "0.15"
---

# Section One {.sdaia-dark background-gradient="linear-gradient(135deg, #1C355E, #00C9A7)"}

## Key Point {.sdaia-dark background-color="#1C355E"}

::: {.callout-important}
## The Rule
Critical information here.
:::

. . .

:::: {.columns}
::: {.column width="50%"}
**Left Column**
- Point one
- Point two
:::
::: {.column width="50%"}
**Right Column**
- Point three
- Point four
:::
::::

## Animated Content {auto-animate=true}

::: {data-id="concept"}
**Core concept.**
:::

## Animated Content Expanded {auto-animate=true}

::: {data-id="concept"}
**Core concept.** Now with additional explanation.
:::

::: {.fragment .fade-up}
::: {.callout-tip}
## Key Takeaway
Important insight revealed on click.
:::
:::

## Activity Slide {.sdaia-dark background-color="#00C9A7"}

### Instructions

1. Step one
2. Step two
3. Step three

⏱️ **Time: 10 minutes**

## Questions? {background-gradient="linear-gradient(135deg, #1C355E, #9B8EC0)"}

::: {.r-fit-text}
Thank You
:::
```
