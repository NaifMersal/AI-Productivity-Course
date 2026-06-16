## **Course Title: AI at Work: Build the Workflows That Win Back Your Week**

*A 3-day workshop to turn the work you repeat into reusable, measurable AI workflows — run by an AI agent that works as a permanent member of your operations team.*

**The Delivery Loop:** **Show** (Instructor high-energy demo) → **Build** (Students apply a workflow to a real task from their backlog) → **Refine** (Group critique of the business logic).

**The Running Spine:** On Day 1 every participant writes an **Automation Backlog** (the recurring tasks that eat their week) and starts a simple **Time Log**. Every build session, they pull one task from that backlog, build a workflow for it, and record the before/after time. By the finale they total it into **hours won back per week** — the proof the course worked.

**The Primary Stack:** The hands-on tool is the **Hermes desktop agent** (Projects, `CLAUDE.md`/`AGENTS.md`, Skills, Memory, Cron, Connectors). But the **concepts are portable** — every feature is taught as *the general idea → how Hermes does it → what other apps (ChatGPT, Gemini, Claude, Coworker) call it*. Students leave able to operate one coherent agent, not juggle ten tools.

> See `prompts/automation_backlog_and_time_log.md` for the worksheet participants fill in throughout, and `../chunks/reference/mental_model_and_agent_concepts.md` for the plain-language definitions behind every concept below.

> **Structure: Foundation + Expansion.** Day 1 is the **Foundation** — the portable core,
> single-sourced as concept chunks in the repo-root `chunks/` library and shared with every
> SDAIA workshop (e.g. `ksu-workshop/`). The Day-1 decks `{{< include >}}` those chunks and
> wrap them with manager examples. Days 2–3 are the **Expansion**: each session builds on a
> Foundation artifact (context pack → `CLAUDE.md`; RICE → Skill; grounding → narrative/data).

---

### **Day 1 — Foundation: Think Like an AI-Native**

**Goal:** Stop treating AI as a search engine. Understand *how* it actually works — the two layers, what "context" really is — so the agent you build on Day 2 makes sense instead of feeling like magic. Leave with reusable delegations, not one-off answers. *(Composed from the shared `chunks/` library.)*

#### **Course Kickoff — Welcome & Your Automation Backlog (09:00 – 09:20)**

*   **Win Back Your Week:** the running spine — every build session automates one task from your list, and the finale totals the hours saved. (No mindset lecture: the *how it works* shift lands in the next session via the two layers.)
*   **Where AI Pays Off:** The bottleneck test — repetitive, data-heavy, drafting, and predictable work first; high-stakes, deeply human, confidential, or originality-driven work with caution. The "good fit" work is exactly what goes on the backlog.
*   **Build (Deliverable):** Each participant lists **3–5 recurring tasks** as their **Automation Backlog** and logs current time-per-task in the **Time Log**. This is the target list for the rest of the course.

#### **How AI Actually Works — The Two Layers (10:00 – 11:00)**

*   **The Keystone Concept:** When you "talk to AI" you're really talking to **two layers stacked together**.
    *   **The Model Layer — "the brain in a jar":** brilliant but with **total amnesia**. Stateless. Knows nothing about you; just predicts the next word; forgets everything when the request ends.
    *   **The App Layer — "the office around the brain":** stores your info in files/a directory and **re-sends the relevant pages on every single request**. *This* is what makes AI feel like it remembers.
*   **What "context" really is:** everything the app stacks on the brain's desk before it works. **Quality is mostly a context problem, not a smartness problem.**
*   **The "desk" has limits (context window):** why long chats start "forgetting," and why saved instructions beat re-pasting.
*   **What a "script" is:** saved, repeatable steps run the same way every time — for exact work the *agent* writes and runs it as real code; *you* never write any. Demystify the word before Day 2.
*   **The Payoff:** Once you see the two layers, `CLAUDE.md`, Projects, Memory, and Skills stop being mysterious — they're all just the app getting smarter about **what to re-send**.
*   **Build (from your backlog):** Take a task and write a short "context pack" for it — the standing facts the AI would need every time. (This becomes raw material for your `CLAUDE.md` on Day 2.)
*   **Micro-Check:** Live Quiz: "Which layer do you fix?" (wrong tone every time vs. a made-up fact).

#### **Delegating to AI — The RICE Pattern + Advanced Moves (11:15 – 12:30)**

*   **The Reframe:** Stop chatting. Start delegating. You don't need a chatbot — you need a direct report.
*   **The Pattern:** Give AI what you'd give a new hire — **Role, Instructions, Context, Examples** (RICE) — so you get a usable result on the first pass. (Note how *Context* is the same thing you mapped in the two-layers session.)
*   **Instructor Demo:** Building a **Client Relationship Assistant** live.
    *   *Scenario:* Messy notes from a call with "Lisa" where a deal was almost lost to a vague follow-up.
    *   *Solution:* A structured delegation that turns the notes into: Summary, Decisions, Action Items (Owner/Deadline), Clarifications Needed.
*   **Advanced Moves (for when AI fumbles a smart question):** by default it answers fast and shallow — these slow it down.
    *   **Think step by step** *(Chain of Thought)* — show the reasoning before the answer. Best for logic, math, scheduling.
    *   **Debate it out** *(Tree of Thoughts)* — argue from several expert viewpoints, then synthesize. Best for strategy and judgment calls.
    *   **Double-check** *(Self-Consistency)* — solve it independently a few times and flag disagreement. Best for numbers and data extraction.
*   **Safety First — the "Newspaper Test":** *Context* is the most powerful part of RICE and the most dangerous to paste raw. Never upload what you wouldn't want on the front page; apply **Data Sanitization** (anonymize names/secrets) before any upload.
*   **Build (from your backlog):** Write a RICE delegation for a recurring "messy input → clean output" task, then add the matching advanced move to a decision or calculation task. Log the time saved.
*   **Micro-Check:** Live Quiz: spot the missing RICE element; match the problem type to the right advanced move; and identify the "Safe vs. Risky" prompt.

#### **Grounding AI in Truth — The Research Workflow (13:30 – 15:00)**

*   **The New Workflow:** Start with **context**, not a blank page. Stop reading 100 pages by hand. (The cleanest proof of the two layers: when you control the context, you control the answer.)
*   **The Trust Layer:** Upload your sources (PDFs, docs) so the assistant answers **only** from them and **cites its work** — the antidote to hallucinations.
*   **Tools in Action:** Hermes (upload + cite from your files) as the primary; **NotebookLM** / **Deep Research** / **Project Knowledge** as portable alternatives.
*   **Build (from your backlog):** "The 10-Hour Research Task in 10 Minutes." Upload a complex document and produce a verified 1-page executive summary. Log the time saved.
*   **Micro-Check:** Live Quiz on choosing the right tool and the safety check before uploading.

---

### **Day 2 — Expansion: Meet Your Agent — Build Your Hermes Operations Team**

**Goal:** Turn the Foundation's mental model into a real, persistent agent. Install it, give it a home and standing instructions, teach it reusable Skills, and give it Memory — so it stops being a chat window and becomes a teammate that already knows your rules. **Full hands-on, in a sandbox.** *(Each session upgrades a Day-1 Foundation artifact.)*

#### **Meet Hermes — Setup & Your First Agent Run (09:00 – 10:30)**

*   **From chat to agent:** the difference between a chat box and an agent that can open files, run steps, and act.
*   **Setup (hands-on):** install the **Hermes desktop agent**; meet the **working directory** — the actual folder on your computer where your context lives. ("So *that's* the 'directory' the app saves everything in.")
*   **Where things live:** a quick, non-scary tour — your files, your standing-instructions file, your saved Skills, your Memory. Nothing is magic; it's all just files in a folder.
*   **Agent-Era Safety — the second rule:** the Newspaper Test guarded what you *paste in*; **Blast Radius & Human-in-the-Loop** guards what the agent *does*. Always start in **draft / notify-me mode** before **act-on-its-own mode**. All course work runs in a **sandbox folder with dummy data**.
*   **Build:** give the agent its first real (sandboxed) task end-to-end and watch it work across files, not just chat.
*   **Micro-Check:** Live Quiz: "act now" vs. "propose and wait" — which mode for which task?

#### **Projects & Standing Instructions — `CLAUDE.md` / `AGENTS.md` (10:45 – 12:15)**

*   **The "Groundhog Day" Problem:** a great one-off delegation is forgotten the moment the chat closes. Productivity comes from **reuse**, not re-typing.
*   **A Project = a dedicated office:** one workspace per body of work, with its own files, so the agent pulls *that* context and not everything else.
*   **The wall note — `CLAUDE.md` / `AGENTS.md`:** the standing instructions the agent reads at the start of every job (who you are, tone, rules, formats). **Two filenames, one idea**; other apps call it *custom instructions* or *system prompt*. **This is the single biggest lever** — fix something here once, fixed forever.
*   **Build (hands-on):** create a Project and write your first `CLAUDE.md` from the "context pack" you drafted on Day 1 (the two layers). Prove it: ask for something with **zero** restated context and watch it land in your voice.
*   **The ROI:** ~5 minutes to set up once vs. minutes saved on every future run — log the recurring saving against your backlog item.
*   **Micro-Check:** Live Quiz: which belongs in `CLAUDE.md` vs. a one-off message?

#### **Skills — Your Reusable Workflow Library (13:15 – 14:45)**

*   **From delegation to capability:** turn the RICE delegation from Day 1 (RICE) into a **saved Skill** the agent runs on command — the agent-era successor to a "Gem"/"GPT"/saved prompt.
*   **Anatomy of a Skill (in plain language):** a name, when to use it (the trigger), and the steps — a book the agent pulls and opens only when the task calls for it. No code.
*   **Instructor Demo:** build **"The Executive Briefer"** — paste raw notes, get a board-ready decision memo — then save it as a Skill and run it on a *completely different* scenario to prove it remembers.
*   **Build (from your backlog):** package one recurring task as a Skill, run it twice on different inputs, and log the recurring weekly saving.
*   **Don't over-engineer:** Skills for recurring tasks; plain chat for true one-offs.
*   **Micro-Check:** Live Quiz: Skill or one-off chat?

#### **Memory — Teaching the Agent to Remember You (15:00 – 16:30)**

*   **The notebook:** persistent facts the agent keeps **across sessions** — your role, preferences, recurring projects — and re-sends when relevant.
*   **Memory vs. `CLAUDE.md`:** the wall note is rules you *set*; memory is facts the agent *accumulates*. When to use which.
*   **Your default persona:** set Role, Tone, and Format once so the agent always sounds like **you**, not a robot — across every Project.
*   **Build (hands-on):** seed the agent's Memory with your working style and a few standing facts; start a fresh session and confirm it carries them over.
*   **Safety beat:** memory is context too — keep it sanitized; nothing in the notebook you wouldn't want re-sent.
*   **Micro-Check:** Live Quiz: belongs in Memory, in `CLAUDE.md`, or neither?

---

### **Day 3 — Expansion: Agents That Act — Executive Output & ROI**

**Goal:** Let the agent work on its own and on your real tools, then point the whole stack at board-ready output and conversations with your data — and total the hours you've won back.

#### **Cron & Connectors — The Agent That Acts on Its Own (09:00 – 10:45)**

*   **The autonomous leap:** from *a tool you operate* to *a teammate that acts on a schedule*.
*   **Cron — the standing appointment:** schedule the agent to run a task automatically ("every Friday 4pm, draft the weekly status").
*   **Connectors — the keys:** securely link the agent to **Gmail / Google Calendar / Google Drive** so it can fetch and act on real data, not just talk. (MCP is the standard; the acronym is optional.)
*   **Guardrails first (non-negotiable):** every Cron and Connector starts in **draft / notify-me mode**; promote to **act-on-its-own** only after it has proven itself. Mind the **blast radius**.
*   **Build (hands-on, sandboxed):** stand up one scheduled job in notify-me mode (e.g., a daily inbox triage that *drafts* replies) and connect one read-only data source. Log the recurring time it will save.
*   **Micro-Check:** Live Quiz: spot the unsafe automation (what could it do if it's wrong, and who'd catch it?).

#### **From Notes to Narrative — The Amazon Method + Design Engine (11:00 – 12:30)**

*   **The Problem:** "The Frankenstein Deck." Slides pasted from five files with no coherent story.
*   **The Solution:** **The Amazon Memo Method** — narrative first, visuals second.
    *   *Step 1: The Draft.* Write the 1-page narrative (the pitch).
    *   *Step 2: The Roast.* Ask the agent to act as a skeptical CFO and attack the logic ("think step by step").
    *   *Step 3: The Blueprint.* Convert the refined narrative → slide outline → visual descriptors.
*   **The Design Engine (speed & polish):** turn the blueprint into a board-ready deck in minutes.
    *   *Method A — One-Click (Gamma):* paste outline → generate deck.
    *   *Method B — Corporate-Safe (Word/Markdown → PowerPoint):* outline → official template, zero manual formatting.
*   **Build (from your backlog):** "The Emergency Board Update." It's 11:50 AM; the board meets at 12:00. From raw crisis notes, produce a roasted narrative **and** a 5-slide on-brand deck. Log the time saved.
*   **Micro-Check:** Live Quiz on why we write before we design.

#### **Interviewing Your Data (13:30 – 15:00)**

*   **Conversational Analysis:** Skip VLOOKUP and pivot tables — ask your data questions like a colleague.
    *   "What is our fastest-growing expense category?"
    *   "Summarize the spending trends for Q3 vs Q2."
*   **Extract & Enrich:** Pull structured data from a receipt image (OCR), then reconcile it against the expense export.
*   **"What If" Scenarios:** Model budget changes on the enriched data.
*   **Build (from your backlog):** Run a real "interview" on `hermes-agent-course/data/expenses_export.csv`. Log the time saved vs. building formulas.
*   **Micro-Check:** Live Quiz on conversational command structures.

#### **The ROI Finale + Your Workflow Library (15:15 – 16:30)**

*   **The Stack, end to end:** Research → Delegate → Project + `CLAUDE.md` → Skills → Memory → Cron + Connectors. The full pipeline you now operate.
*   **Your Workflow Library:** package your best Skills so a teammate could run them tomorrow — your own library of books, and the habit of reaching for it at each bottleneck.
*   **ROI Calculation:** Total your **Time Log**: **(Task Frequency × Duration × % AI Efficiency)** = hours per week won back.
*   **Showcase:** 3-minute presentation — "The one process I will never do manually again."
*   **Micro-Check:** Final Quiz on the two layers, the agent stack, and course ROI.
