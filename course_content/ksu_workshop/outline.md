# Building Your Own AI Assistant — KSU Faculty Workshop (4 hours)

A single-session, hands-on workshop for **King Saud University (KSU) faculty members**.
It is a condensed, retooled adaptation of the 3-day **"AI at Work"** course in this repo.
By the end, each participant leaves with a working **AI assistant** they have set up
themselves, plus 2–3 automations applied to their own academic work.

## Differences from the parent course

- **Hands-on tool:** **Claude Cowork** (Anthropic's desktop agent) — chosen because it is
  the easiest to set up. *(Official product name is "Cowork," not "Coworker.")* Concepts
  stay portable (ChatGPT, Gemini, Claude, NotebookLM mentioned as alternatives).
- **Audience flavor:** examples are academic/faculty (lecture notes → slides, summarize
  research papers, grade-summary calculations, committee-report drafting, syllabus prep),
  not the parent course's Saudi-finance business cases.

## Delivery loop

Same as the parent course: **Show** (instructor demo) → **Build** (faculty apply it to a
real task) → **Refine** (quick group critique). Aim for ~70% hands-on, ~30% theory. All
hands-on agent work runs in a **sandbox folder with dummy data**.

## The two safety rules (carried throughout)

1. **Newspaper Test** — guards what you *paste in* (sanitize student data, unpublished
   research, exam content first).
2. **The Undo Test / Human-in-the-Loop** (industry term: *blast radius*) — guards what the agent *does*; start every
   Skill / scheduled job in **draft / notify-me** mode before letting it act on its own.

## Structure

The workshop runs as **two teaching sessions, each followed by a hands-on practice block**,
then NotebookLM and a wrap-up. Slide decks are number-free; the **canonical order lives in
`slides/index.qmd`** (a plain landing page that links each deck). The "what's a script"
concept is taught **with automation** (where Cowork actually writes scripts), not up front.

## Time budget (≈240 min, including a 10-min break)

| Block | Deck | Mins |
|---|---|---|
| Welcome + agenda | `overview.qmd` | 10 |
| Session 1 — How AI works + RICE | `how_ai_works_and_rice.qmd` | 45 |
| Practice 1 — foundations use-cases | `practice_foundations.qmd` | 25 |
| — break — | *(end of `practice_foundations.qmd`)* | 10 |
| Session 2 — Cowork + Automation (Skills/Schedule/Scripts) | `cowork_and_automation.qmd` | 50 |
| Practice 2 — automation use-cases | `practice_automation.qmd` | 30 |
| NotebookLM — grounding + slides | `notebooklm_grounding_and_slides.qmd` | 40 |
| Wrap-up + ROI | `wrap_up.qmd` | 30 |

## Sessions

### Session 1 — How AI Works + RICE (`how_ai_works_and_rice.qmd`)
- **Objectives:** understand the **two layers** (model = "brain in a jar", app = "the
  office"); know the model's limits (amnesia, hallucination, the finite "desk"); then
  **delegate instead of ask** with **R**ole, **I**nstructions, **C**ontext, **E**xamples;
  one emphasized advanced move — **double-check** (Self-Consistency) for grades/totals —
  with "think step by step" / "debate it out" named in passing.
- **Demos:** same question with/without grounding → why context decides quality; messy
  committee notes → a clean student email via a full RICE prompt.
- **Note:** the "script" concept is **not** taught here — it now lives in Session 2.

### Practice 1 — Delegate a Real Task (`practice_foundations.qmd`)
- **Build:** each faculty member writes one full RICE prompt for a recurring "messy → clean"
  task, then adds the matching advanced move to a calculation/judgment task.
- **Refine:** "I like / I wish / I wonder." **Ends with the 10-minute break.**

### Session 2 — Meet Cowork + Automating Your Work (`cowork_and_automation.qmd`)
- **Objectives:** chat vs. agent; the **working directory** (the real folder = the office);
  install/open Cowork, run a first end-to-end task; the second safety rule (the undo test /
  blast radius); then **Skill** = a book in your library opened by a trigger; **`/schedule`** =
  a standing appointment (start notify-me); **script** (defined here) = Cowork writing/running
  a small script for a repeatable calculation — no coding.
- **Demos:** "read these three files → one summary"; Build-a-Deck Skill (notes → `.pptx`);
  a grade-summary calculation from a CSV via a generated script; a scheduled weekly digest, notify-me.

### Practice 2 — Build Your First Workflows (`practice_automation.qmd`)
- **Build:** point Cowork at the sandbox and run one real task in propose mode; package one
  recurring task as a Skill and invoke the trigger twice on different inputs; optionally
  schedule a notify-me digest.
- **Refine:** "I like / I wish / I wonder"; log minutes saved × times per week.

### NotebookLM — Grounding & Creating (`notebooklm_grounding_and_slides.qmd`)
- **Objectives:** **grounding** ("based only on these sources" + citations); NotebookLM's
  **slide creation** (Detailed Deck vs. Presenter Slides, `.pptx` export, Revise editing,
  pre-generation steering); when to use Cowork vs. NotebookLM vs. Deep Research.
- **Demo / Build:** upload a real (safe) paper/policy PDF → grounded summary → presenter deck; log time.

### Wrap-up — Your AI Assistant + ROI (`wrap_up.qmd`)
- **Objectives:** recap the toolkit (RICE → Cowork → Skills/Schedule/Scripts → NotebookLM);
  tally **hours won back per week**; next steps; restate the two safety rules.
- **Activity:** "I like / I wish / I wonder" feedback.

## Reuse map (parent-course sources)

- `course_content/reference/mental_model_and_agent_concepts.md` — canonical definitions.
- `course_content/slides/session_2_two_layers.qmd` + `session_3_delegating_with_rice.qmd` → Session 1
- `course_content/slides/session_5_meet_hermes.qmd` (+ `session_6`, `session_7`, `session_9`) → Session 2 (Hermes→Cowork)
- `course_content/slides/session_4_grounding_research_workflow.qmd` (+ `session_10`) → NotebookLM
- `prompts/automation_backlog_and_time_log.md` → Wrap-up time-saved tally
- The "script" concept (formerly opening Session 1) now lives in Session 2, next to where Cowork writes scripts.
