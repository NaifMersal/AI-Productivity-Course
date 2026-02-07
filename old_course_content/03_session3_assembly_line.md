# Session 3: The Assembly Line (Manual Chaining)

**Duration:** 1.5 Hours
**Goal:** Understand workflow logic by manually chaining steps (Step 1 Output -> Step 2 Input).

---

## 13:00 - Part 1: The Logic of Workflow (15 min)

**Bridge from Session 2:**
> "In Session 2, we built a Project that handles Role and Context automatically. A one-sentence prompt now works because the Project does the heavy lifting.
>
> But we only ran ONE task. Real business processes aren't one step—they're **chains**. The output of Step 1 feeds into Step 2, which feeds into Step 3.
>
> Today we learn to chain. First manually (to feel the pain), then in Session 4 we'll automate it."

**The Core Rule:**
> "The OUTPUT of Step N becomes the INPUT of Step N+1."

**Concept:** Processes are Chains.
**Instructor Script:**
> "Business isn't just one question. It's a pipeline. You analyze data -> write a draft -> edit the draft -> format the report. The output of Step 1 is the input of Step 2."

---

## 13:15 - Part 2: Instructor Demo - The Manual Chain (4 Steps) (15 min)

**Scenario:** Skill Acquisition Chain.
**Pre-requisite:** Use the "Skill Acquisition Planner" Project from Session 2. Ensure `personal_profile.md` is in Project Knowledge.

### Step 0: The Trigger (User Request)
User Input:
> "I want to learn Python for automating my month-end close process in 8 weeks with 3 hours/week."

### Step 1: Gap Analysis
**Prompt:**
```text
Analyze the "Personal Profile" in the Project Knowledge.

Perform a Gap Analysis between his Current Skill Set vs. his Learning Goals.
Output a table showing: Current Skill Level, Required Skill Level, and the "Gap".
```
**Expected Output:** A table identifying gaps like "Python Syntax", "Pandas Dataframes", "Data Cleaning logic".
![Gap Analysis](assets/session3_gap_analyisis.png)

### Step 2: Learning Path
**Prompt:**
```text
Based on the Gap Analysis above, create a sequential Learning Path.
Break this down into Phases, for each phase, list specific sub-skills he must master.
```
**Expected Output:** A structured list of phases and topics.
![Learning Path](assets/session3_step2_learning_path.png)

### Step 3: Resource Curation
**Prompt:**
```text
Based on the Learning Path and the profile, curate a list of specific resources.

Suggest 3 specific courses, books, or documentation sites that fit this style.
```
**Expected Output:** A list of resources like "Automate the Boring Stuff", "Pandas Cookbook", etc.
![Resources](assets/session3_step3_resourse_curation.png)

### Step 4: Schedule
**Prompt:**
```text
Based on the Resources selected and Ahmed's time constraints (3 hours/week mid-month, blackout during first 5 days), create a realistic 8-week study schedule.
Map specific resources to specific weeks.
Include "Buffer Weeks" for month-end close periods where no studying happens.
```
**Expected Output:** A calendar-like view of what to study when.
![Schedule](assets/session3_step4_schedule.png)

---

## 13:30 - Part 3: Student Build (Manual) (45 min)

**Activity:** Manually chain all 4 steps of YOUR process in a single chat.

> **Note:** To maximize LLM performance/reasoning power, we normally open a **New Chat** for each step (to clear context). However, for this simple example, we will do it in one single chat to demonstrate the flow.

1.  **Identify 3-4 steps** in your business process (e.g., Summarize -> Extract Dates -> Write Email).
2.  **Step 1:** Run Step 1 in your Project. -> **Get Output.**
3.  **Step 2:** **Take the result**, and manually ask for Step 2 (referencing Step 1). -> **Get Output.**
4.  **Step 3:** **Take the result**, and manually ask for Step 3 (referencing Step 2).
5.  **Step 4:** **Take the result**, and manually ask for Step 4 (referencing Step 3).

*Tip: If the AI loses track, remind it of the context or the previous step's output.*

---

## 14:15 - Part 4: The Friction (15 min)

**Discussion:**
*   "Did anyone get lost?"
*   "Did the AI forget what happened in Step 1 by the time you got to Step 4?" (Context Drift).
*   "Did you find yourself copy-pasting or repeating instructions?"

**Transition:**
> "This 'Human Router' method is slow and error-prone. Keeping the chain in your head is hard. We need a map—an SOP that holds the logic so you don't have to."

---

## ☕ Break (15 Minutes)
