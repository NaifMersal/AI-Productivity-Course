# AI Productivity at Work — Win Back Your Week (3 days)

A 3-day, hands-on workshop for **employees** (any office role — no technical background
needed). Each participant leaves with a working **AI assistant** they set up themselves,
**3–5 reusable workflows** applied to their own recurring tasks, and a measured number:
**hours won back per week**. They also leave with a map of the wider AI tool landscape so
they know what else is out there.

It is a sibling of the repo's other SDAIA offerings (`ksu-workshop/`, `hermes-agent-course/`)
and shares the same **Foundation** — the concept chunks in the repo-root `chunks/` library.

## Differences from the sibling courses

- **Audience:** general employees. Examples are everyday office work — status reports,
  meeting notes, customer emails, expense summaries, vendor comparisons — not KSU's academic
  flavor or the Hermes course's executive/board framing.
- **Hands-on tool:** **Claude Cowork** (Anthropic's desktop agent) — chosen because setup is
  simplest. Taught **portably**: *the general idea → how Cowork does it → what other apps
  (Antigravity, Hermes, ChatGPT) call it.* Hermes is named as the option for more technical
  staff. We show one tool; the workflow transfers.
- **One new brief** vs. the Foundation: **Pick Your AI & Expand Your Toolkit** (Day 3) — the
  app landscape (chat vs. agent, the chat trio, the agents) and the wider tools map folded
  into one short, hands-on brief before the finale. (Chat-vs-agent is also taught on Day 2
  in `meet_cowork.qmd`, so Day 1 carries no survey deck.)

## Delivery loop

**Show** (instructor demo) → **Build** (apply a workflow to a real backlog task) → **Refine**
(quick group critique, "I like / I wish / I wonder"). Aim ~70% hands-on, ~30% theory. All
hands-on agent work runs in a **sandbox folder with dummy data**.

## The running spine

On Day 1 every participant writes an **Automation Backlog** (3–5 recurring tasks that eat
their week) and starts a **Time Log**. Every build session pulls one task from that backlog,
builds a workflow for it, and records before/after time. The finale totals it into **hours
won back per week**. Worksheet: `prompts/automation_backlog_and_time_log.md`.

## The two safety rules (carried throughout)

1. **Newspaper Test** — guards what you *paste in*. Sanitize confidential or personal data
   before it goes anywhere.
2. **Blast Radius / Human-in-the-Loop** — guards what the agent *does*. Start every Skill,
   schedule, and connector in **draft / notify-me** mode before letting it act on its own.

## Structure: Foundation + Expansion

Day 1 is the **Foundation** — the portable core, single-sourced as concept chunks in
`chunks/` and shared with every SDAIA workshop. Day-1 decks `{{< include >}}` those chunks
and wrap them with employee examples, and close on a hands-on Build (the grounded summary)
rather than a survey. Days 2–3 are the **Expansion**: each session builds on a Foundation
artifact (context pack → standing instructions; RICE → Skill; grounding → narrative/data),
then ends with one short app/tool-landscape brief and the ROI total.

Decks use **descriptive, numberless slugs**; the canonical order lives here and in
`index.qmd`, not in filenames.

---

## Day 1 — Foundations: Think Like an AI-Native

*Composed from the shared `chunks/` library + employee examples.*

| # | Block | Deck | Mins |
|---|---|---|---|
| 0 | Welcome & Your Automation Backlog | `kickoff.qmd` | 30 |
| 1 | How AI Actually Works — The Two Layers | `two_layers.qmd` | 75 |
| 2 | Delegating to AI — RICE + Advanced Moves + Newspaper Test + peer Refine | `delegating_rice.qmd` | 120 |
| 3 | Grounding AI in Truth — The Research Workflow | `grounding.qmd` | 75 |

### Kickoff — Welcome & Your Automation Backlog (`kickoff.qmd`)
- Running spine; the **Bottleneck Test** (what work to hand AI); two safety rules preview.
- **Build:** list 3–5 recurring tasks + current minutes-per-task in the Time Log.

### Session 1 — How AI Works: The Two Layers (`two_layers.qmd`)
- Includes `_two_layers`, `_context`, `_context_window`. (The `_script` concept is **not**
  taught here — it moves to Session 7, where the agent actually writes one.)
- Employee examples; payoff slide ("everything is the app deciding what to re-send").
- **Build:** write a short "context pack" for one backlog task (raw material for Day-2
  standing instructions).

### Session 2 — Delegating with RICE (`delegating_rice.qmd`)
- Includes `_rice`, `_advanced_moves`, `_newspaper_test`.
- Demo: messy meeting notes → a clean recap email (Summary / Decisions / Action Items).
- Advanced moves (think step by step / debate it out / double-check); Safe-vs-Risky check.
- **Build:** write a full RICE delegation for a recurring "messy → clean" task; add the
  matching advanced move to a numbers/judgment task.
- **Refine:** swap prompts with a neighbor — *I like / I wish / I wonder* (the Refine half of
  the loop, now on-slide). The brief becomes raw material for a Day-2 Skill.

### Session 3 — Grounding in Truth (`grounding.qmd`)
- Includes `_grounding`. Context-first rule; "no citation = didn't happen"; NotebookLM and
  Deep Research as the truth-layer tools.
- **Build:** turn a long (safe) document into a verified 1-page summary.

---

## Day 2 — Meet Your Agent: Build Your Cowork Operations Team

*Full hands-on, in a sandbox. Each session upgrades a Day-1 Foundation artifact.*

| # | Block | Deck | Mins |
|---|---|---|---|
| 4 | Meet Cowork — Setup & Your First Agent Run | `meet_cowork.qmd` | 90 |
| 5 | Projects & Standing Instructions (`AGENTS.md` / `CLAUDE.md`) | `projects_and_standing_instructions.qmd` | 90 |
| 6 | Skills — Your Reusable Workflow Library | `skills.qmd` | 90 |
| 7 | Memory — Teaching the Agent to Remember You | `memory.qmd` | 75 |

### Session 4 — Meet Cowork (`meet_cowork.qmd`)
- Chat vs. agent; the **working directory** = the office; three-click setup.
- Second safety rule: **blast radius / human-in-the-loop**; sandbox + dummy data.
- **Build:** point Cowork at the sandbox, run a first end-to-end task ("read these three
  status updates → one summary").

### Session 5 — Projects & Standing Instructions (`projects_and_standing_instructions.qmd`)
- The "Groundhog Day" problem; a **Project** = a dedicated office; **`AGENTS.md` / `CLAUDE.md`**
  = standing instructions on the wall (two filenames, one idea; other apps: custom
  instructions). The single biggest lever.
- **Build:** create a Project and write a first standing-instructions file from the Day-1
  context pack; prove it with a zero-context request.

### Session 6 — Skills & Scripts (`skills.qmd`)
- From a RICE delegation to a **saved Skill**; anatomy (name / trigger / steps); a book the
  agent opens only when needed. Demo: a "Status Roll-Up" or "Meeting Recap" Skill.
- **Script taught here, just-in-time:** Skill (instructions the agent *reads and follows*) vs.
  Script (code it *writes and runs* to compute exactly). Demo: "Expense Crunch" on
  `data/expenses_export.csv` — totals, outliers, summary sheet. This is Day 1's "saved,
  repeatable steps," now done as real code; no coding by the participant.
- **Build:** package one recurring backlog task as a Skill; run it twice on different inputs.

### Session 7 — Memory (`memory.qmd`)
- The agent's notebook: persistent facts across sessions; Memory vs. standing instructions;
  your default persona. Safety: memory is context too — keep it sanitized.
- **Build:** seed Memory with your working style; start a fresh session and confirm carry-over.

---

## Day 3 — Agents That Act: Executive Output, the Wider Toolkit & ROI

| # | Block | Deck | Mins |
|---|---|---|---|
| 8 | Schedule & Connectors — The Agent That Acts on Its Own | `schedule_and_connectors.qmd` | 90 |
| 9 | From Notes to Narrative — The Amazon Method + Design Engine | `notes_to_narrative.qmd` | 75 |
| 10 | Interviewing Your Data | `interviewing_your_data.qmd` | 75 |
| 11 | **Pick Your AI & Expand Your Toolkit** *(new — brief + try one tool)* | `tools_landscape.qmd` | 30 |
| 12 | The ROI Finale + Your Workflow Library | `roi_finale.qmd` | 60 |

### Session 8 — Schedule & Connectors (`schedule_and_connectors.qmd`)
- **Schedule / Cron** = a standing appointment; **Connectors** = keys to Gmail / Calendar /
  Drive (MCP is the standard; the acronym is optional). Guardrails first: draft / notify-me.
- **Build:** stand up one notify-me scheduled job (e.g. a daily inbox triage that *drafts*).

### Session 9 — From Notes to Narrative (`notes_to_narrative.qmd`)
- The "Frankenstein Deck" problem; the **Amazon Memo Method** (Draft → Roast → Blueprint);
  the design engine (Gamma one-click vs. corporate Word/Markdown → PowerPoint).
- **Build:** raw notes → a roasted 1-page narrative **and** a 5-slide on-brand deck.

### Session 10 — Interviewing Your Data (`interviewing_your_data.qmd`)
- Conversational analysis (skip VLOOKUP/pivots); OCR a receipt; "what if" scenarios.
- Callback: for exact math the agent **writes and runs a script** (the Session-6 concept,
  reinforced where it actually executes).
- **Build:** interview `data/expenses_export.csv`; reconcile `data/Shawarma_House_Receipt.png`.

### Session 11 — Pick Your AI & Expand Your Toolkit (`tools_landscape.qmd`) *(new — merged brief)*
- Folds the former app-landscape and tools-landscape surveys into **one short brief**:
  **chat vs. agent**; the chat trio (ChatGPT / Claude / Gemini) and agents (Cowork /
  Antigravity / Hermes) at a glance; the curated tools map **by job-to-be-done** (voice,
  video, image, slides/design, meetings/notes, writing, automation glue); the Newspaper Test
  stated **once**; an optional local-LLM stretch slide (awareness only).
- **Build (hands-on, ~5 min):** pick **one** new app/tool, Newspaper-Test it, run **one** real
  prompt from your own work, and judge whether it beats your current tool. **Refine:** share
  with a neighbor — *I like / I wish / I wonder.*

### Session 12 — The ROI Finale (`roi_finale.qmd`)
- The full stack end to end; package your **Workflow Library**; total the Time Log:
  **Frequency × Duration × % AI Efficiency = hours/week won back**; 3-minute showcase.

---

## Reuse map (sources)

- `chunks/_*.qmd` — Foundation concepts, included into Day-1 decks (path `../../chunks/`).
- `chunks/reference/mental_model_and_agent_concepts.md` — canonical definitions.
- `ksu-workshop/slides/cowork_and_automation.qmd` + `notebooklm_grounding_and_slides.qmd` —
  closest Cowork-flavored sources for Day 2 + grounding.
- `hermes-agent-course/slides/*.qmd` — structure for projects, skills, memory, cron,
  notes-to-narrative, interviewing-data, roi-finale (retarget Hermes → Cowork, manager →
  employee).
- `prompts/automation_backlog_and_time_log.md` — the running-spine worksheet.
- `notes/tools_examples.md` — candidate list behind the new tools-landscape deck.
