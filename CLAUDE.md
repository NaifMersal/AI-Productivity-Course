# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Layout

This repo holds **one shared library of Arabic (RTL) slide decks** plus **one small page per
workshop**. There is no build step and no template/generated split: every `.qmd` you open is
the real thing, and you edit it directly.

```
slides/          the deck library. FLAT. every deck, shared by every workshop.
data/            sample files for the follow-alongs. root is neutral and shared.
data/gov/        the government track's sample files.
data/edu/        the academic track's sample files.
handouts/        printable participant material for the in-person tracks.
assets/          instructor extras (the .skill bundle, screenshots). not rendered.
office.qmd       a workshop: title, duration, station table.  guide: outline.md
ksu.qmd          a workshop: same.                            guide: outline.md
gov5.qmd         five days, in person, government employees.  guide: outline-gov5.md
edu5.qmd         five days, in person, faculty.               guide: outline-edu5.md
index.qmd        the portal linking every workshop and every deck.
slides_template/ SDAIA brand assets, applied globally by _quarto.yml.
notes/           planning notes and the Arabic voice style guide.
notes/grounding/ fetched source packs behind every tool claim that reaches a slide.
notes/reference/ vendored reference material. sdaia-dictionary.md is grep-only, never read whole.
scripts/         helper scripts. make_redirects.py keeps pre-restructure URLs alive.
```

There are no per-audience deck subfolders. A subfolder is a licence to duplicate: the same
idea ends up taught twice under two flavours with neither copy maintained. `slides/` was
split once, into `slides/gov/`, and it produced exactly that. It stays flat.

**Old URLs are kept alive at render time.** The site used to publish one folder per
workshop (`office-workshop-ar/…`, `ksu-workshop/…`). `scripts/make_redirects.py` runs as a
Quarto `post-render` step and writes a meta-refresh stub at each old page path, pointing at
the new page. Nothing from the old tree is republished. The deck list in that script is
**pinned, not globbed** (`LEGACY_DECKS`): only the nine slugs that genuinely published under
the old tree get stubs, because a glob over today's flat library would mint stubs at URLs
that never existed. Renaming one of those nine kills its old URL, and the script warns you at
render time. Don't delete the `post-render` line in `_quarto.yml`, and don't add a slug to
`LEGACY_DECKS` that never shipped under the old tree. Old QR codes point at those paths.

**A workshop is an index page.** `office.qmd`, `ksu.qmd`, `gov5.qmd` and `edu5.qmd` differ
only in title, subtitle, duration, audience framing, and which decks they list, in what order,
for how long. To add a workshop: copy a workshop page, write its intro deck, change the day
tables, add a portal row to `index.qmd`.

**Each workshop owns exactly one intro deck**, named `intro_<workshop>.qmd`. It carries the
day or week arc, the room rules and the promised outcome, and it **names** the two safety
rules. It teaches no concept. Grandfathered exception: `overview.qmd` is the short track's
intro and keeps its filename, because `make_redirects.py` protects `overview.html`.

## One flat library, neutral by default

**What varies between workshops is exactly two things:** the workshop page, and the intro
deck it opens with. Everything else in `slides/` is written so an office employee, a
government employee and a faculty member all recognize the example: meeting notes → recap
email, a departmental event with a plan and a decisions log and a task list, a report reviewed
against a checklist, an expense sheet summarized by category. Do **not** reintroduce
audience-specific flavour (sales, CRM, campaigns, leads, grading, syllabi, classification
tiers) into a neutral deck. If an example only lands for one audience, it belongs in a
workshop page, an intro deck, or a registered deck below.

**Concepts are single-sourced by construction.** Every workshop renders the same `slides/`, so
editing a concept once updates every workshop. There is no parity rule to maintain.

### The flavour register

A non-intro deck may carry audience flavour **only if it is listed here**, with a front-matter
comment naming the track it is exclusive to. An unregistered deck that drifts flavoured is a
defect. This register is the only guard the flat library has: read it before editing a shared
deck, and re-read it before each delivery.

| Deck | Exclusive to | Why the flavour is load-bearing |
|---|---|---|
| `local_models_lab.qmd` | gov5 | The offline drill only lands on a genuinely restricted document. |
| `hermes_desktop_lab.qmd` | gov5 | Same: an agent on a disconnected machine is a government premise. |
| `team_adoption_plan.qmd` | gov5, edu5 | The department is the unit of adoption; the neutral version is empty. |
| `data_and_trust.qmd` | gov5 | Its payoff slide promises the restricted file returns on the local-AI day. Only gov5 has one. |
| `where_your_data_goes.qmd` | gov5 | Same: its residency ladder ends at «الجلسة القادمة», which is `local_models_lab`. |
| `from_objectives_to_materials.qmd` | edu5 | Learning outcomes are the subject, not decoration. |
| `active_learning_design.qmd` | edu5 | Class activities and role-play only exist for a teacher. |
| `teaching_media.qmd` | edu5 | «متى يستحقّ الصوت مكانه في مقرّر» is the whole question. |
| `course_ta_project.qmd` | edu5 | A TA answering students from lecture material. |
| `academic_integrity_assessment.qmd` | edu5 | Assessment design and grading authority. |
| `students_and_ai.qmd` | edu5 | Addressed at what you tell your students. |
| `choosing_your_tool.qmd` | edu5 | Registered for one reason: the hallucination specimen is a fabricated **academic citation**. The criteria half is neutral and this deck is the best candidate to split and de-flavour. |
| `beyond_the_chat_box.qmd` | edu5 | Only its Project example (syllabus, lectures, rubric) is flavoured. Cheap to neutralise when a second track wants it. |

`context_and_tokens.qmd` and `personal_data_law.qmd` are deliberately **not** registered: both
are written neutral and both are wanted by gov5. Keep them that way. PDPL in particular is a
national law, not audience flavour, and every article it quotes is grounded in
`notes/grounding/pdpl.md`.

**A registered deck's flavour is rarely just vocabulary. It is usually a promise about the
week.** `data_and_trust` and `where_your_data_goes` read audience-neutral sentence by sentence,
and were caught only because each ends by promising a session that exists in one track. When
checking a deck against this register, read its **last** slide first: that is where a deck
tells you which workshop it thinks it is in.

Eleven registered decks against nine neutral ones is a lot, and it is the honest state rather
than a target. The last two rows are marked as de-flavouring candidates precisely so the
register does not become a place where flavour goes to be forgiven.

**`data/` mirrors this.** The root is neutral and shared. `data/gov/` and `data/edu/` carry
flavour, and may only be named by a workshop page or a registered deck. A neutral deck never
hard-links a track folder: it says «الملف الذي وزّعه المدرِّب» and lets the workshop page name
the file.

## In-person tracks (gov5, edu5)

Two of the four workshops are five-day, in-person programs: `gov5.qmd` (government employees,
guide `outline-gov5.md`) and `edu5.qmd` (faculty, guide `outline-edu5.md`). Both reuse the
shared decks unedited and add their own. Three rules govern them.

**The in-person delivery loop is Show → Build → Refine**, not the online track's
Show → Mirror → Take home. Online forced 3-minute follow-alongs because open practice is
where remote learners drop out; in person that constraint is gone. Target ~70% hands-on: a
short concept beat, then a real build block, then peer review. A deck written for these tracks
that reads like a lecture is wrong for them.

**One new capability per day, not one new document type.** An earlier draft of the gov track
spent a day each on correspondence, reports, meetings, and spreadsheets. That is one skill in
four costumes, and it was cut. Document work is *lab material*; it is never a topic of its
own. gov5 runs foundations → work mode → local AI → vibe coding → capstone. edu5 runs
foundations → content and active learning → building course tools → responsible use →
students and showcase.

**Tool claims are grounded, never recalled.** Decks that name a product are authored from
fetched vendor documentation recorded in `notes/grounding/`, with the exact quote, canonical
URL, and fetch date behind every command and number that reaches a slide. Third-party blog
posts about these tools are already demonstrably wrong. Any command printed on a slide must
have been executed; anything absent from the source pack gets flagged in the deck rather than
guessed. Prefer teaching the **concept** and naming the product afterwards, or showing it
live: a slide asserting what a product's interface does rots the week it ships, and every such
assertion needs its own citation. Re-verify the pack before each delivery.

## Project Overview

This section and the Course Schedule Reference below describe the **short online track**
(`office.qmd`, `ksu.qmd`), the repo's original product. The two five-day in-person tracks are
covered above and in their own outlines.

**بناء مساعدك الذكي الخاص** (Building Your Own AI Assistant) — a ~2.5 hour hands-on Arabic
workshop teaching people to use AI as a permanent member of their team, not as a search
engine. By the end each participant has handed real work to an AI assistant themselves and
leaves with a one-page recipe. Decks describe what the session does. They never promise hours
saved or sell an outcome.

**Hands-on tool:** **Claude Cowork** (Anthropic's desktop agent), chosen because it is the
fastest to set up. Concepts stay **portable** (ChatGPT, Gemini, Claude, Gemini Notebook named
as alternatives). The audience is non-technical: **nobody writes code.**

Delivered **online**. The loop is **Show** (instructor runs a real task end to end) →
**Mirror** (everyone repeats a small piece at the same time, from a provided prompt and file)
→ **Take home** (the same task on their own work, from the recipe). All hands-on agent work
runs on the provided sample files, never real data.

## Slides

Slides are SDAIA-branded Quarto reveal.js decks. Branding is applied globally in the root
`_quarto.yml`, so each deck's front matter stays minimal (`title` / `subtitle` / `date` /
`lang: ar` / `dir: rtl` / `format: revealjs` with `rtl: true`). Author, render, preview,
screenshot, and visually verify them with the **`author-verify-slides`** skill — branding and
Quarto patterns are constant across SDAIA slide projects.

Run Quarto from the repo root; it finds `_quarto.yml` there and mirrors the source path into
`output/` (e.g. `slides/overview.qmd` → `output/slides/overview.html`). `output/` is
gitignored.

- Render everything: `quarto render`
- Render one deck: `quarto render slides/<deck>.qmd`
- Preview with live reload: `quarto preview slides/<deck>.qmd`
- Render + screenshot + verify branding/overflow:
  `python .claude/skills/author-verify-slides/driver.py slides/<deck>.qmd --all --reveal-all`

## Core Teaching Framework

**The Two Layers** (the keystone, introduced in the first concept deck) — the mental model
everything else hangs off. The **model layer** is a "brain in a jar": stateless, knows nothing
about you, just predicts the next word, forgets everything when a request ends. The **app
layer** is the "office around the brain": it stores your info in a directory and **re-sends
the relevant context on every request**. Once learners see this, the working directory,
Skills, and grounding stop being magic — they're all the app getting smarter about *what to
re-send*. The Two Layers slides live in `slides/how_ai_works_and_rice.qmd`; reuse their
analogies verbatim across decks.

**Project** (right after the context window) — the concrete, clickable instance of the app
layer, and the middle rung between a disposable prompt and a Cowork Skill: a saved workspace
(ChatGPT / Claude / Gemini) holding **standing instructions + uploaded files**, re-sent on
every chat inside it. It is the one takeaway that needs **no install**, so it lands even for
learners who never set up Cowork. It also pre-frames two later concepts — Project folder →
**working directory**, standing instructions → **Skill**.

**Agent-stack vocabulary** (the work-mode module) — taught with the analogy first, the term as
a label: **working directory** (the real folder Cowork points at = the office), **Skill** (a
book in the office library, pulled and opened only when the task calls for it),
**`/schedule`** (a standing appointment; industry term **Cron**), **Connector / MCP** (giving
the agent keys to email/calendar/drive). A **script** is "saved, repeatable steps":
instructions the *agent* writes and runs as real code for exact, repeatable work; you never
write or see code. A Skill is instructions the agent *reads and follows*; a script is code it
*runs to compute*. A **Template** is a real file on the learner's machine, their **PowerPoint
template** (`.pptx`) or spreadsheet, the on-brand layout the script *fills*; the worked
example is notes → an editable `.pptx`, never a revealjs/Quarto deck (that's authoring jargon
this audience never sees). The keystone framing is **composition**: a Skill bundles a script
and a template behind one trigger, and **Schedule / Connectors just run a Skill** (on a clock,
or with keys). They're not new kinds of thing.

**RICE Pattern** — the delegation pattern:

- **R**ole: Who should the AI be?
- **I**nstructions: What exactly should it do? (includes format, length, tone rules)
- **C**ontext: What information should it have? (the same "context" defined earlier)
- **E**xamples: A sample of the desired output (few-shot prompting)

**Advanced moves** — taught in plain language, with the industry term kept as a label so
learners recognize it: **think step by step** (Chain of Thought), **debate it out** (Tree of
Thoughts), **double-check** (Self-Consistency). Lead with the plain-language move, not the
jargon.

**Two safety rules** — **Newspaper Test** (guards what you *paste in*; sanitize first) and,
once agents can act, **Blast Radius / Human-in-the-Loop** (guards what the agent *does*; start
every Skill / scheduled job / connector in draft / notify-me mode before act-on-its-own). All
hands-on agent work runs on the **provided sample files**.

## Content Authoring Guidelines

When generating or modifying course content:

- Use management-friendly analogies; avoid technical jargon without explanation.
- Follow the "Explain → Demonstrate → Practice → Apply" cycle.
- Prefer a mental model plus *when/how to use it* over frameworks, ladders, and matrices.
- Cut taglines, slogans, imagined-quote bubbles, and any sentence that only restates the box
  above it. One concept box and one concrete example per slide.
- Every concept deck ends in a knowledge check; the three work-mode decks also end in a
  follow-along.
- Use the "I like, I wish, I wonder" feedback framework.
- Keep examples audience-neutral unless the deck is in the flavour register above.

### Slide voice and density

These are acceptance criteria for any slide you write or edit. The Arabic wording contract is
`notes/arabic-voice-style-guide.md`, whose §3 carries the same density rules.

Three things in that guide outrank everything on this page. **§4 program commitments**: no
unsourced claim ever reaches a slide, the limits note stays wherever products are named, and
nothing says the AI decides or is accountable. **§2** makes
`notes/reference/sdaia-dictionary.md` the arbiter for any Arabic technical term the guide's own
table doesn't fix — grep it, it is 7,600 lines. **§6** is the divergence register against the
sibling SAMAI 2 program: read it before "fixing" a wording inconsistency, because several are
deliberate. Background in `notes/samai2-comparison.md`.

**Density**

1. Max **~40 words of prose per slide**. Quoted prompts, the recipe card, the RICE specimen
   prompt, and the run-of-show table are *reference artifacts, not prose*: they are exempt and
   stay verbatim. Cut the explanation wrapped around them instead.
2. Max **two content blocks** per slide (a card plus one list or one line). Not card +
   paragraph + list + centered restatement + callout.
3. Bullets are **fragments, not sentences**: ≤8 words, no semicolons, no gloss clause.
4. **Delete any centered closer that only restates the card above it.**
5. **No inline `font-size:` shrink hacks.** A shrink means the slide is too full; cut text
   until the theme's type scale fits. `_quarto.yml` sets `scrollable: false`, so overflow is
   clipped silently, never scrolled.
6. **Cut before splitting.** Split a slide only when the idea needs two beats, and give the
   new slide the same `data-id` so `auto-animate` still pairs.

**Voice**

7. **No em-dash (`—`) as a connective**, and never in a slide title. It was this repo's
   default connective and read as machine-written. Use a full stop, or a colon when the label
   is real.
8. Retire the `**Bold term** — gloss` list template. No two lists in a deck share the same
   grammar.
9. At most **one antithesis per deck** ("not X, but Y"), only where the contrast is the
   teaching point. No "Picture an…", no "Think of it as…", no `*(industry term: X)*`
   parenthetical (name the term once in the body instead).
10. Slide titles are plain statements in sentence case. No chiasmus, no two-sentence
    imperatives, no tagline that repeats the title. Section dividers (`#`) keep title case.
11. **Teach each idea once**, and the concept deck owns the full statement. اختبار الجريدة is
    stated in full in `how_ai_works_and_rice`, bound to the **C** of RICE; اختبار التراجع in
    `cowork_intro`, bound to the moment an agent can act. Intro decks **name and promise**
    both rules in one line each; they never state them. Every other deck references them by
    name.

Prefer the existing SCSS vocabulary over new inline styles: `.card` + `.accent-teal|purple|
orange|navy|yellow`, `.card-dark`, `.fill-*`, `.center`, `.tight`, `.muted`, `.pill`, `.qbox`.
These use `border-inline-start` and mirror correctly under RTL; hardcoded `border-left` /
`text-align: left` do not.

## Course Schedule Reference (≈135 min core, ≈2.5 hrs with margin)

Canonical order lives in the workshop pages (`office.qmd`, `ksu.qmd`) and `outline.md`. Deck
slugs are descriptive and numberless. The work-mode module is **three teaching decks plus the
recipe**, one concept each, each of the three ending in a knowledge check *and* a
follow-along.

1. **Overview** (`overview.qmd`) — welcome + agenda + the two safety rules (5 min)
2. **How AI Works & Writing Great Prompts** (`how_ai_works_and_rice.qmd`) — Two Layers +
   context + **Project** + RICE + advanced moves + Newspaper Test (30 min)
3. **Practice — Delegate a Real Task** (`practice_foundations.qmd`) — RICE on a real task,
   then save it into a Project; ends with the 10-min break (15 + 10 min)
4. **From Chat to Work Mode** (`cowork_intro.qmd`) — the keystone of the module: asking
   *about* the work vs. handing *over* the work; working directory = office; the second safety
   rule (undo test / blast radius); instructor demo + follow-along (20 min)
5. **Build It Once** (`skills_scripts_templates.qmd`) — Skill (book) → Script (exact numbers)
   → Template (the layout) → composition. **Demo, not a build block**; ends in a follow-along
   where learners paste a provided Skill and run it (20 min)
6. **How Far This Goes** (`how_far_this_goes.qmd`) — Schedule **and** Connectors merged: both
   just *run a Skill*, on a clock or with keys; wider blast radius; module key takeaways
   (15 min)
7. **Your Recipe** (`recipe.qmd`) — the one-page take-home: three prompts they already watched
   work, to run on their own files; both safety rules; pick which to run first (10 min)
8. **Your AI Assistant** (`wrap_up.qmd`) — recap + name one recurring task to try first +
   safety (10 min)

**Optional station, listed last:** **Grounding & Creating with Gemini Notebook**
(`notebooklm_grounding_and_slides.qmd`) — grounding + citations + slide creation (+40 min).
Run it only if the core finishes early. It sits at the end so any overrun lands there instead
of cutting the assistant-building payoff.

### Online delivery: follow-alongs, not practice blocks

The workshop is delivered **online**, where an open practice block is the thing learners opt
out of. So the doing is dissolved into the flow: decks 4–6 each end in a **3-minute
follow-along**, a **provided prompt on a provided file**, run by everyone at once, with
exactly one obvious outcome. The rule: **if it can fail live, it isn't a follow-along.** The
instructor demo must be *replicable* — the exact prompt appears on screen and again in the
recipe. Real practice happens async from the recipe card; setup (app install + sample files)
is **pre-work**, not session time.

The delivery loop is therefore **Show → Mirror → Take home**, not Show → Build → Refine.
