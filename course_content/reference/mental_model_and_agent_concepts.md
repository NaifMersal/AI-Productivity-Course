# The Mental Model & Agent Concepts (Plain-Language Reference)

This is the **canonical, jargon-free reference** for the ideas the course is built on.
It is the source of truth for the slides — especially **Session 2 ("How AI Actually
Works: The Two Layers")** and the **Day 2 agent-stack sessions**. If a term shows up in a
deck, define it here first and reuse the same analogy everywhere.

**Audience:** non-technical managers and professionals. Nobody writes code. The goal is
that when a learner sees `CLAUDE.md`, "Project," "Skill," "Memory," "cron," or "connector"
in any app, they already know what it *is* and *why it exists*.

**Stack note:** The course's primary hands-on tool is the **Hermes desktop agent**
(Projects, `CLAUDE.md`/`AGENTS.md`, Skills, Memory, Cron, Connectors). But the **concepts
are portable** — every term below is taught as *the general idea → how Hermes does it →
what other apps call it*. We mention **Coworker** and other apps as alternatives, not
replacements.

---

## Part 1 — The One Big Idea: Two Layers

Everything in the course hangs off a single insight. When you "talk to AI," you are
actually talking to **two different things stacked together**.

### The Model Layer — "the brain in a jar"

- **The analogy:** A brilliant graduate's brain floating in a jar. It has read most of the
  internet, so it's clever — but it has **total amnesia**. It knows nothing about *you*,
  your company, or even what you said five minutes ago. The instant it finishes answering,
  it forgets everything.
- **What it really is:** The AI model is **stateless**. It does not "remember" and it does
  not "look things up." All it does is **predict the next word** based on the text it was
  just handed. (This is the same "prediction engine" from Session 1 — the reason it can
  *hallucinate*: when it doesn't know, it predicts a plausible-sounding word anyway.)
- **Why a manager cares:** The model is not a database and not a coworker with a memory.
  Anything you want it to "know," you have to **hand it every single time**. That single
  fact explains the entire rest of the course.

### The App Layer — "the office around the brain"

- **The analogy:** The brain in a jar is useless on its own — it can't open files, keep
  notes, or remember your name. So we build an **office** around it: filing cabinets, a
  notebook, a standing to-do list. Every time you ask for something, the office **gathers
  the relevant pages and hands them to the brain along with your request** — then files the
  answer back. The brain still has amnesia; the *office* is what makes it feel like it
  remembers.
- **What it really is:** The app (ChatGPT, Gemini, Claude, the **Hermes** agent…) is the
  software wrapped around the model. It **stores your information in files/a directory** and
  **re-sends the relevant parts on every request**. The "memory," "projects," and "custom
  instructions" features you see are all the app doing this gathering-and-resending for you.
- **Why a manager cares:** When something works or breaks, you can now tell **which layer**
  to fix. Wrong tone every time? That's the *app layer* (your standing instructions), not
  the brain. A made-up fact? That's the *model layer* guessing — verify it.

> **The sentence to remember:** *The model knows nothing and forgets everything; the app
> re-sends what matters on every request.* Every feature below is just the app getting
> smarter about **what to re-send**.

---

## Part 2 — The Core Vocabulary

For each term: the **analogy**, **what it really is**, and **why a manager cares**.

### Context

- **Analogy:** Everything the office stacks on the brain's desk before it starts a job — your
  request *plus* the background pages it needs to do it well.
- **What it really is:** All the text sent to the model along with your question — your
  instructions, pasted documents, standing rules, relevant memory. The model's entire
  "world" for that one request.
- **Why a manager cares:** **Output quality is mostly a context problem, not a smartness
  problem.** A weak answer usually means weak context, not a weak model. "Give it context"
  is the whole skill.

### Context window — "the desk"

- **Analogy:** The brain's desk has a **fixed size**. You can only fit so many pages on it
  at once. Pile on too much and older pages fall off the edge.
- **What it really is:** The maximum amount of text the model can consider at one time.
  When a conversation gets too long, the earliest parts drop out of view.
- **Why a manager cares:** Explains why a long chat starts "forgetting" the beginning, and
  why **saved instructions beat re-pasting** — the app puts the important pages back on the
  desk for you every time, so they never fall off.

### Script

- **Analogy:** A **recipe card** of steps written down once so the job runs the same way
  every time — whether a person or the agent follows it.
- **What it really is:** Saved, repeatable instructions. In this course a script is
  **plain-language steps**, not programming. (Under the hood some scripts are code, but
  **you never write code in this course** — you describe the steps.)
- **Why a manager cares:** Demystifies the word. A "script" isn't a programmer thing — it's
  just *"do these steps, in this order, every time."* That's the foundation of every
  workflow you'll build.

### Project

- **Analogy:** A **dedicated office (or folder)** for one body of work, with its own filing
  cabinet of relevant documents — separate from your other work.
- **What it really is:** A named workspace that bundles related files and instructions so
  the app pulls *that* context (and not everything else) into requests about that work.
- **Why a manager cares:** Keeps work from bleeding together. "Q3 Board Report" and "Vendor
  Contracts" each get the right background without you re-explaining.

### `CLAUDE.md` / `AGENTS.md` — "standing instructions pinned to the wall"

- **Analogy:** The **note pinned to the office wall** that the brain reads at the **start of
  every job**: who you are, your tone, your rules, your formats.
- **What it really is:** A plain-text file the app automatically includes at the top of
  every request in that project. `CLAUDE.md` and `AGENTS.md` are just **two filenames for
  the same idea**; other apps call it *custom instructions* or a *system prompt*.
- **Why a manager cares:** **This is the single biggest lever.** Fix the tone, format, or a
  recurring rule here **once**, and it's fixed for every future request — no re-typing,
  no reminding.

### Skill — "a saved recipe card the agent can pull out"

- **Analogy:** A **recipe card filed in the office**. You say "make the quarterly summary"
  and the agent pulls the card and follows it — you don't re-explain the steps.
- **What it really is:** A named, reusable workflow saved into the agent that it can invoke
  on command. The agent-era successor to a "Gem" (Gemini) / "GPT" (ChatGPT) / saved prompt.
- **Why a manager cares:** This is how a one-time good delegation becomes a **permanent
  capability**. Build it once; run it forever with a single phrase.

### Memory — "the notebook the agent keeps about you"

- **Analogy:** A **notebook** where the office jots down lasting facts about you — your role,
  your preferences, your recurring projects — and flips back to it on future visits.
- **What it really is:** Persistent facts the app stores **across sessions** and re-sends
  when relevant, so you don't restate them each time.
- **Why a manager cares:** The agent stops feeling like a stranger every morning. It's the
  difference between a temp and an assistant who's worked with you for a year.

### Cron / scheduled agent — "a standing appointment"

- **Analogy:** A **standing appointment** on the agent's calendar. "Every Friday at 4pm,
  draft the weekly status." It just happens — you didn't have to ask.
- **What it really is:** A schedule that triggers the agent to run a task automatically on a
  timer, with no human in the chat at that moment.
- **Why a manager cares:** This is the leap from *a tool you operate* to *a teammate that
  acts on its own*. It's also exactly why the safety rules below get stricter.

### Connector (MCP) — "giving the agent keys"

- **Analogy:** Handing the agent the **keys** to your inbox, calendar, and drive so it can
  actually fetch and do things — not just talk about them.
- **What it really is:** A secure link between the agent and a real tool (Gmail, Google
  Calendar, Google Drive, etc.) so it can read and act on real data. (MCP is the technical
  standard; you don't need to know the acronym.)
- **Why a manager cares:** It's where AI stops being a chat box and starts touching your
  real work — which is powerful, and the reason "blast radius" matters.

---

## Part 3 — Safety in the Agent Era (two rules, not one)

The original course had **one** safety rule. An agent that can *act* needs a **second** one.

### Rule 1 — The Newspaper Test (guards what you *put in*)

- **The rule:** Before pasting anything into AI, ask: *"If this appeared on the front page
  of the newspaper, would I be fired or sued?"* If yes or maybe — **don't paste it.**
  **Sanitize** first: anonymize names, generalize numbers, strip identifiers.
- **What it guards:** Your **inputs** — the confidential data leaving your hands.

### Rule 2 — Blast Radius & Human-in-the-Loop (guards what the agent *does*)

- **The rule:** Before letting an agent act on its own, ask: *"What's the worst thing this
  could do if it gets it wrong — and who would notice in time?"* Start every Skill, Cron, or
  Connector in **draft / notify-me mode** (it proposes, you approve) before ever promoting it
  to **act-on-its-own mode**.
- **What it guards:** The agent's **actions** — a misfired email, a wrong calendar change, a
  deleted file. The Newspaper Test never saw this coming because nothing got *pasted*; the
  agent *did* something.
- **In practice (course rule):** All Day-2/Day-3 hands-on work runs in a **sandbox folder**
  with **dummy data**, so a mistake can't touch real work while you're learning.

> **The pair to remember:** *Newspaper Test* = watch what goes **in**. *Blast Radius* =
> watch what comes **out** as an action.

---

## Part 4 — How the pieces fit (one picture)

```
        YOU ──ask──▶  [ APP LAYER  =  the office ]  ──hands a full desk──▶  [ MODEL = brain in a jar ]
                          • gathers your context                              • reads the desk
                          • CLAUDE.md (wall note)                             • predicts the next words
                          • Project (the right folder)                        • forgets it all afterward
                          • Memory (the notebook)                                     │
                          • Skill (the recipe card)                                   │
                          • Connector (the keys) / Cron (the calendar)                ▼
        YOU ◀──answer/action──────────────────  files the result back  ◀──────────────
```

Read it as one sentence: **you ask, the office loads the right context onto the desk, the
amnesiac brain predicts an answer from what's on the desk, and the office files the result
and carries out any action.** Projects, `CLAUDE.md`, Memory, Skills, Cron, and Connectors
are all just the office getting better at **what to load and what to do with the answer**.
