# Course Title: AI Operations for MIS/IS Managers: From Prompt to Process

## **The Dual-Track Strategy:**
1. **Instructor Demo:** "Personal Skill Acquisition Planner" 
2. **Student Project:** Their real business challenges (Procurement automation, report generation, compliance workflows, etc.)

---

## 📧 PRE-COURSE (1 Week Before)

### Email to Participants:
* **Account Setup:**
  * Create Claude account (Pro/Teams - specify requirement)
  * Login credentials verification
* **Pre-Work Assignment:**
  * Identify your business process using the template provided
  * **CRITICAL: Data Sanitization**
    * Redact ANY sensitive personal data (names, SSNs) or secrets (API keys, passwords) from your documents.
    * Replace real names with placeholders (e.g., "Client A", "Technician 1").
  * Gather 1-2 *sanitized* relevant documents (strategy docs, policy files, sample reports)
  * Complete the "Process Identification Worksheet"
* **Tech Check:** 
  * Login to Claude
  * Create a test Project
  * Upload a test document


---

## DAY 1: Foundations & Architecture

### Opening: The Setup & Safety First (30 Minutes)

**Session Objectives:**
* Understand the "delegation" vs. "chatbot" mindset
* **CRITICAL:** Apply Data Safety & Anonymization standards
* Set up Claude Projects workspace
* Upload foundational documents

**Content:**
* **09:00:** Welcome & Logistics
* **09:05: Data Safety Breakdown (The "Newspaper Test")**
  * *Rule:* "Don't put anything in the chat you wouldn't want on the front page of the newspaper."
  * *Action:* Anonymize documents BEFORE uploading. (Replace names with "User ID", redact financials).
* **09:15:** **The "Manager's Mindset" Reveal**
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
*   Architect a "Claude Project" to act as a permanent context engine
*   Distinguish **Global RCTC** (Project Instructions) from **Local RCTC** (Chat)
*   Automate your context to achieve "One-Sentence Delegation"

**Content:**
*   **Part 1: The "Lazy Manager" Philosophy (15 min)**
    *   *Concept:* DRY (Don't Repeat Yourself).
    *   **Short-Term Memory (Context Window):** This is the active "conversation" (The Chat). It resets every time.
    *   **Long-Term Memory (Project Knowledge):** This is the "Brain" (The Project). It persists forever.
    *   *Goal:* Move Context from the "Chat Window" (Ephemeral) to the "Project" (Permanent).
*   **Part 2: Building the Brain (45 min)**
    *   **Instructor Demo:** Setting up the "Global Role" & Uploading "Global Context".
    *   **Student Build:** Create the Project for *their* specific business process.
*   **Part 3: One-Sentence Delegation (15 min)**
    *   **Execution:** Run a *short, simple* prompt inside the Project.
    *   *Result:* High-quality output because the Project handled the complexity.

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
*   "Install" the SOP into the Project Brain (The Process Lobe)
*   Execute complex workflows with "One-Sentence Delegation"

**Content:**
*   **Part 1: The "Playbook" (30 min)**
    *   *Concept:* The SOP is the written version of the Manual Chain we just built.
    *   **Instructor Demo:** Uploading `skill_sop.md` to the Project.
*   **Part 2: Automated Execution (45 min)**
    *   **The Payoff:** Run `Execute the entire Skill Acquisition Process for Ahmed.`
    *   *Result:* The AI follows the SOP automatically because it's in the Project Knowledge.
    *   **Teaching Point:** "In Session 3, YOU were the glue. In Session 4, THE SOP is the glue. You moved yourself out of the loop."
*   **Part 3: Peer Logic Check (15 min)**
    *   Swap SOPs. "If I used this map, where would I get lost?"
*   **Part 4: Day 1 Wrap (15 min)**
    *   **Homework:** "Identify one 'Edge Case' that might break your SOP."



---

## DAY 2: Engineering & Operations

### Session 5A: Day 1 Debrief (15 Minutes) 

**Content:**
* Rapid-fire: What worked? What edge case did you find?
* **Update Project Knowledge:**
  * "Take your SOP from yesterday (Session 3) and upload it to your Claude Project."
  * This commits your "Process Map" to the AI's long-term memory.
* *Goal:* Transition immediately to "making it bulletproof".

---

### Session 5B: Operational Readiness - Skill Packaging (1.75 Hours)

**Learning Objectives:**
* Package workflows as Claude Skills for team deployment
* Implement Version Control for Prompts
* Run end-to-end stress test of the full workflow

**Content:**
* **Phase 1: Packaging as a Claude Skill (45 min)**
  * *Concept:* Skills = Reusable, Shareable Prompt Templates
  * *Demo:* Instructor packages the "Skill Planner" workflow as a Skill:
    * **Skill name and description** - Clear, action-oriented naming
    * **System prompt** - Combining R-C-T-C elements into a single instruction set
    * **Input variables** - What the user provides (e.g., `[SKILL]`, `[TIMEFRAME]`)
    * **Output format expectations** - Structured deliverables
  * *Activity:* Students create a Skill from their Step 1 prompt:
    * Define the Skill's purpose and trigger
    * Set up the system instructions
    * Test with a colleague

* **Phase 2: Version Control (30 min)**
  * *Concept:* Prompts are Code. They degrade if changed randomly.
  * **Create `prompts.md` Library:**
    * Create a new artifact (file) in your Project called `prompts.md`.
    * Store your "Golden Prompts" here with version numbers.
  * **Version Log:**
    * V1.0 - Initial Draft
    * V1.1 - Added Safety Check (Date)
    * V2.0 - Packaged as Skill (Date)

* **Phase 3: Final Logic Check (30 min)**
  * Run the full process end-to-end with the packaged Skill + Safety Checks.
  * Ensure the "Handoffs" still work.

*Transition:* "Your Skill works. But does it work SAFELY? Let's add the guardrails."

---

### ☕ Break (15 Minutes)

---

### Session 6: Advanced Risk & Compliance (1.25 Hours) 
**Learning Objectives:**
* Create safety checklists for organizational use
* Identify "Red Zones" where AI is forbidden

**Content:**
* **Part 1: Data Safety Review (15 min)**
  * Recap functionality of masking/anonymization from Day 1.
* **Part 2: Organizational Safety & SOPs (45 min)**
  * **Activity:** Students add a "Safety Check" step to their SOP.
  * *Discussion:* How to enforce this in a team?
* **Part 3: When NOT to Use AI (15 min)**
  * Legal documents, Final hiring decisions, Non-consensual data.

**Reflection:** "Where is the 'Human in the Loop' in your process?"

---

### 🍽️ Lunch Break (1 Hour)

---

### Session 7: Optimization & Advanced Engineering (1.75 Hours)

**Learning Objectives:**
* Use Advanced Prompting (CoT, Few-Shot) to optimize packaged Skills
* Implement "Parallel Option Generation" (Tree of Thought) for better decisions
* Refine prompt logic for higher quality outputs

**Content:**
* **Part 1: The "Power Tools" (30 min)**
  * *Concept:* When R-C-T-C isn't enough.
  * **One-Shot / Few-Shot:**
    * *Problem:* AI tone is generic.
    * *Fix:* Give it 2 examples of *perfect* past reports. "Write like this."
  * **Chain of Thought (CoT):**
    * *Problem:* AI makes logic errors.
    * *Fix:* "Think step by step." (Force the model to show its work).
  * **Parallel Option Generation / Tree of Thought (ToT):**
    * *Problem:* AI gives one answer, but you need to compare options.
    * *Fix:* "Generate 3 approaches, then recommend one."

* **Practice Exercises (10-15 min each):**
  * **Few-Shot Mini-Lab:** "Here's a generic scenario. Apply few-shot prompting to match this tone/style."
  * **CoT Challenge:** "Debug this flawed logic prompt using step-by-step reasoning."
  * **ToT Exercise:** "Generate 3 parallel options for this decision point, then compare."

* **Part 2: Student Optimization (45 min)**
  * "Take your packaged Skill from Session 5B. Apply one of these power tools to make it better."
  * **A/B Test / Quality Rubric:** Compare V1 (Packaged Skill) vs V2 (Optimized).
    * Score both versions (1-5) on:
      * **Accuracy:** Facts/Data correct?
      * **Format:** Followed constraints?
      * **Tone:** Professional/On-brand?
      * **Completeness:** Missed any inputs?
  * **Update `prompts.md`:** Record V2.0 with the optimization applied

---

### ☕ Break (15 Minutes)

---

### Session 8: Solution Showcase (1.5 Hours)

**Learning Objectives:**
* Present completed workflows to peers
* Identify cross-applicable techniques
* Calculate ROI and efficiency gains

**Content:**
* **Part 1: The ROI Calculation (20 min)**
  * **Before/After Analysis Template:** 
    * Time spent manual vs Time spent AI-assisted.
    * *Example:* "3.5 hours savings per role x 10 roles = 35 hours saved."
* **Part 2: Gallery Walk (60 min)**
  * **Solution Showcase:** 3-5 different business processes (Finance, HR, Ops, IT).
  * Everyone learns: "If THAT can be automated, what about THIS?"
  * Instructor ties back: "I showed you a skill planner. You built procurement workflows, report generators. The METHOD is identical."
* **Part 3: Management Highlights & Closing (10 min)**
  * Instructor highlights: "The Strategist," "The Efficiency Win," etc.

### Closing & Certification (30 Minutes)

* **Certification Requirements:**
  * ✓ Functional Workflow (SOP + Prompts)
  * ✓ Safety Checklist
  * ✓ Completed Claude Skill
  * ✓ ROI Analysis
* **Final Q&A**

---

## 📦 TAKE-HOME MATERIALS
1. **Completed Claude Skill** (shareable with team)
2. **Safety Checklist**
3. **Troubleshooting Guide**
4. **Version Control Template**
5. **Rollout Plan**
6. **ROI Analysis Worksheet**

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

**Day 2:** 9:00 AM - 5:30 PM (8.5 hours)
* Focus: Optimization, Safety, Operations, ROI.

**Total:** 16.5 Contact Hours.