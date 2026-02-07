# Course Title: AI Operations for MIS/IS Managers: From Prompt to Process

## **The Dual-Track Strategy:**
1. **Instructor Demo:** "Personal Skill Acquisition Planner" 
2. **Student Project:** Their real business challenges (Procurement automation, report generation, compliance workflows, etc.)

---

## DAY 1: Foundations & Architecture

### Opening: The Setup & Safety First (45 Minutes)

**Session Objectives:**
* Understand the professional shift AI brings
* Draw inspiration from real-world success stories
* **Live Tech Check:** Verification of accounts and platform access
* **Data Prep:** Identify and sanitize real-world business documents
* **CRITICAL:** Apply Data Safety & Anonymization standards
* Set up Project (Claude/ChatGPT) or Gem (Gemini) workspace

**Content:**
* **09:00:** Welcome & The "Why": How AI is reshaping work
* **09:10:** Inspiration: Real-world Success Stories
* **09:20:** **Tech & Data Setup (The "Workbench")**
  * **Account Check:** Login to Claude/ChatGPT/Gemini.
  * **Project Setup:** Create a new Project or Gem.
  * **Process Identification:** Identify a specific business process to automate.
  * **Data Sanitization (CRITICAL):**
    * Redact sensitive data (names, SSNs, credentials).
    * Replace real names with placeholders ("Client A").
    * *Action:* Upload *sanitized* foundational documents.
* **09:40:** **The "Manager's Mindset" Reveal**
  * *Instructor:* "We aren't learning to 'chat' with a bot. We are learning to **delegate** to a junior PMP who works at 1,000x speed. I will build a structured Project Management Office (PMO) workflow live. You will build your own process alongside me."

---

### Session 1: The Science of Delegation (R-C-T-C) (1.5 Hours)

**Learning Objectives:**
*   Understand why "Search Engine" prompts fail
*   Master the Role-Context-Task-Constraint (R-C-T-C) framework
*   Experience the "Friction" of manual prompting (typing 300 words)

**Content:**
*   **Part 0: Primer - How LLMs "Think" (15 min)**
    *   *Concept:* Prediction vs. Knowledge.
    *   **Not a Database:** The AI is a statistical machine, not a fact retriever. It predicts the next likely word based on training, it doesn't "look up" facts.
    *   *Transition:* "Since it doesn't know facts, YOU must be the Manager."

*   **Part 1: The Trap (10 min)**
    *   **Demo:** "The Bad Delegation" (Vague prompt -> Vague result).
    *   *Concept:* AI needs a Manager, not just a requester.
    *   *Garbage In, Garbage Out:* The model can only reason from the context you give it.
    *   If a conversation starts vague or wrong, that ambiguity compounds.
    *   LLMs tend to anchor on early assumptions, so continuing a broken chat often reinforces errors.
    *   In those cases, restarting with a clearer “manager-style” prompt is more effective than incremental corrections.
*   **Part 2: The Framework (45 min)**
    *   **Instructor Demo:** Building the Perfect Prompt (R-C-T-C).
    *   **Activity:** Write a manual R-C-T-C prompt for your process.
*   **Part 3: The Friction (20 min)**
    *   *Discussion:* "This output is great, but who has time to type this?"
    *   *Transition:* "We need an architecture to handle the 'R' and 'C' automatically."

**Reflection:** "Structure creates quality, but at what cost (time)?"

---

### ☕ Break (15 Minutes)

---

### Session 2: The Workbench (Project Architecture) (1.25 Hours)

**Learning Objectives:**
*   Architect a "Project" (Claude/ChatGPT) or "Gem" (Gemini) to act as a permanent context engine
*   Distinguish **Global RCTC** (Project/Gem Instructions) from **Local RCTC** (Chat)
*   Automate your context to achieve "One-Sentence Delegation"

**Content:**
*   **Part 1: The "Lazy Manager" Philosophy (15 min)**
    *   *Concept:* DRY (Don't Repeat Yourself).
    *   **Short-Term Memory (Context Window):** This is the active "conversation" (The Chat). It resets every time.
    *   **Long-Term Memory (Project/Gem Knowledge):** This is the "Brain" (The Project/Gem). It persists forever.
    *   *Goal:* Move Context from the "Chat Window" (Ephemeral) to the "Project/Gem" (Permanent).
*   **Part 2: Building the Brain (45 min)**
    *   **Instructor Demo:** Setting up the "Global Role" & Uploading "Global Context" (Project/Gem).
    *   **Student Build:** Create the Project/Gem for *their* specific business process.
*   **Part 3: One-Sentence Delegation (15 min)**
    *   **Execution:** Run a *short, simple* prompt inside the Project/Gem.
    *   *Result:* High-quality output because the Project/Gem handled the complexity.

**Reflection:** "I just saved myself 5 minutes of typing for every future request."

### 🍽️ Lunch Break (1 Hour)

---

### Session 3: The Assembly Line (Manual Chaining) (1.5 Hours) 

**Learning Objectives:**
*   Understand workflow logic (Step 1 Output = Step 2 Input)
*   Manually execute a multi-step chain in a single chat (they should split chats if context drifts)
*   Experience the "Context Drift" of long manual chats

**Content:**
*   **Part 1: The Logic of Workflow (15 min)**
    *   *Concept:* Processes are Assembly Lines. The Handoff is critical.
    *   **Instructor Demo:** Manually chaining a 4-step process (Gap Analysis -> Learning Path -> Resource Curation -> Schedule).
*   **Part 2: Student Build (Manual) (60 min)**
    *   **Activity:** Run Step 1. Copy output. Paste into Step 2 prompt. Run Step 2. Continue for all 4 steps.
    *   *Goal:* Feel the friction of copy-pasting and managing context manually.
*   **Part 3: The Friction (15 min)**
    *   *Discussion:* "Did the AI lose context by Step 4? Did you have to repeat instructions?"
    *   *Transition:* "Keeping the chain in your head is hard. We need a map (SOP)."

**Reflection:** "I can build the car by hand, but I'd rather have a factory."

---

### ☕ Break (15 Minutes)

---

### Session 4: Structural Engineering (SOPs & Automation) (1.75 Hours)

**Learning Objectives:**
*   Convert manual "Chains" into a formal Standard Operating Procedure (SOP)
*   "Install" the SOP into the Project/Gem Brain (The Process Lobe)
*   Execute complex workflows with "One-Sentence Delegation"

**Content:**
*   **Part 1: The "Playbook" (30 min)**
    *   *Concept:* The SOP is the written version of the Manual Chain we just built.
    *   **Instructor Demo:** Uploading `skill_sop.md` to the Project/Gem.
*   **Part 2: Automated Execution (45 min)**
    *   **The Payoff:** Run `Execute the entire Skill Acquisition Process for Ahmed.`
    *   *Result:* The AI follows the SOP automatically because it's in the Project/Gem Knowledge.
    *   **Teaching Point:** "In Session 3, YOU were the glue. In Session 4, THE SOP is the glue. You moved yourself out of the loop."
*   **Part 3: Peer Logic Check (15 min)**
    *   Swap SOPs. "If I used this map, where would I get lost?"

* **Packaging as a Skill (Claude Only) (20 min)**
  * *Concept:* Skills = Reusable, Shareable Prompt Templates
  * *Demo:* Instructor packages the "Skill Planner" workflow as a Skill:
    * **Skill name and description** - Clear, action-oriented naming

*   **Part 4: Day 1 Wrap (15 min)**
    *   **Homework:** "Identify one 'Edge Case' that might break your SOP."


---

## DAY 2: Research, Analysis & Personal Productivity

### Session 5: Research & Information Processing (1.5 Hours)

**Learning Objectives:**
*   Synthesize large volumes of information without losing nuance
*   Extract structured insights from unstructured documents
*   **CRITICAL:** Fact-checking and preventing "hallucinations" in professional work

**Content:**
*   **Part 1: The AI Researcher (30 min)**
    *   *Concept:* Moving beyond "TL;DR".
    *   **Techniques:**
        *   *Summarization Constraints:* "Summarize for an executive vs. a technical peer."
        *   *Extraction:* "Pull all dates, dollar amounts, and deliverables into a table."
*   **Part 2: Competitive Intelligence & Market Research (30 min)**
    *   **Activity:** Upload competitor reports/whitepapers.
    *   *Prompt:* "Compare the pricing model of Company A vs Company B based on these files."
*   **Part 3: The Truth Check (30 min)**
    *   **Risk:** AI can sound confident while being wrong.
    *   **Protocol:** Sourcing and Verification. "Cite your sources."
    *   *Hands-on:* Verify a generated claim against the source document.

---

### Session 6: Data & Analysis (Without Code!) (2 Hours)

**Learning Objectives:**
*   Analyze spreadsheet data using plain English exploration
*   Design effective surveys and questionnaires
*   Interpret trends and basic financial scenarios

**Content:**
*   **Part 1: Conversational Data Analysis (45 min)**
    *   *Concept:* "Interviewing" your data.
    *   **Activity:** Upload a dummy sales/budget spreadsheet.
    *   *Prompts:* "What is the fastest growing category?", "Show me the trend for Q3."
    *   *Visuals:* Asking for charts/graphs to visualize the text data.
*   **Part 2: Structure for Input (Survey Design) (45 min)**
    *   *Concept:* Better questions yield better data.
    *   **Activity:** "Create a 5-question employee engagement survey."
    *   *Critique:* Ask AI to critique its own survey for bias.
*   **Part 3: Budget & Scenario Planning (30 min)**
    *   **Activity:** "What if" scenarios.
    *   *Prompt:* "If we reduce marketing spend by 10%, how does that impact the total budget?"

---

### 🍽️ Lunch Break (1 Hour)

---

### Session 7: Personal Productivity Systems (2 Hours)

**Learning Objectives:**
*   Build a "Personal Automation Toolkit"
*   Configure "Custom Instructions" to reduce repetitive prompting
*   Integrate AI into daily workflows (Email, Calendar logic, etc.)

**Content:**
*   **Part 1: Custom Instructions (45 min)**
    *   *Concept:* Setting the "Default Persona" for your AI.
    *   **Activity:** Write your "User Profile" (Role, Tone, Format Preferences).
*   **Part 2: The Prompt Library (45 min)**
    *   *Concept:* Saved "Recipes" for recurring tasks.
    *   **Hands-on:** Create a personal "Prompt Library" (in Excel/Notion) for:
        *   Email polishing
        *   Meeting summaries
        *   Project kickoffs
*   **Part 3: Time-Saving Automations (30 min)**
    *   *Idea Gen:* Brainstorming where AI fits in *your* specific workday.
    *   *Workflow Mapping:* "I get an email -> AI summarizes it -> I draft reply."

---

### ☕ Break (15 Minutes)

---

### Session 8: Solution Showcase (1.5 Hours)

**Learning Objectives:**
*   Demonstrate "Time Back" (ROI) from personal productivity improvements
*   Share "Superpower" workflows with the cohort

**Content:**
*   **Part 1: ROI Calculation (20 min)**
    *   **Worksheet:** Estimate hours saved per week using Day 2 techniques.
    *   *Formula:* (Task Frequency x Duration) x % AI Efficiency = Time Saved.
*   **Part 2: Gallery Walk (60 min)**
    *   **Showcase:** Participants present "The one thing I will automate on Monday."
    *   *Feedback:* Peer review and instructor refinement.
*   **Part 3: Closing (10 min)**
    *   Final thoughts: "You are now the Chief AI Officer of your own desk."

### Closing & Certification (30 Minutes)

*   **Certification Requirements:**
    *   ✓ Completed "Custom Instructions" Profile
    *   ✓ Personal Prompt Library (Min. 3 Prompts)
    *   ✓ ROI Analysis Worksheet
*   **Final Q&A**

---

## 📦 TAKE-HOME MATERIALS
1.  **Personal Prompt Library Template**
2.  **Data Safety Checklist (Updated)**
3.  **"How to Talk to Data" Cheatsheet**
4.  **ROI Calculation Worksheet**
5.  **Course Certificate**

---

## **Updated Materials Needed:**

**Instructor Prep:**
1. **Your Skill Planner prompts** (fully worked example across all sessions)
2. **Process map template** (blank, domain-agnostic)
3. **3-4 "Student Example Stubs"** showing how different roles might apply it:
   * "Finance: Month-End Close Automation"
   * "HR: Onboarding Checklist Generator"
   * "Operations: Incident Response Protocol"

**Student Pre-Work (unchanged concept, clearer examples):**
* "Identify YOUR repeatable business process—not a skill you want to learn, but a TASK you do repeatedly"
* Examples: Weekly reports, vendor evaluations, compliance audits, customer onboarding

---

## ⏰ TIME BUDGET SUMMARY
**Day 1:** 9:00 AM - 5:00 PM (8 hours)
* Focus: Architecture, Process Mapping, Basic Implementation.

**Day 2:** 9:00 AM - 5:45 PM (8.75 hours)
* Focus: Research & Analysis, Personal Productivity, ROI.

**Total:** 16.75 Contact Hours.