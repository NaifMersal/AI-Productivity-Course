# Session 3: The Assembly Line (Manual Chaining)

**Duration:** 30 min demo + 60 min student build

---

## Bridge from Session 2

> "In Session 2, we built a Project that handles Role and Context automatically. A one-sentence prompt now works because the Project does the heavy lifting.
>
> But we only ran ONE task. Real business processes aren't one step—they're **chains**. The output of Step 1 feeds into Step 2, which feeds into Step 3.
>
> Today we learn to chain. First manually (to feel the pain), then in Session 4 we'll automate it."

---

## The Core Rule
> "The OUTPUT of Step N becomes the INPUT of Step N+1."

---

## Demo: 4-Step Chain (Skill Acquisition)

### PRE-REQUISITE
*Use the "Skill Acquisition Planner" Project from Session 2. The `personal_profile.md` should be in Project Knowledge.*

---

### STEP 0: The Trigger (User Request)

```text
I want to learn Python for automating my month-end close process in 8 weeks with 3 hours/week.
```

*This is what the user types. The SOP chain starts here.*


### STEP 1: Gap Analysis

**Prompt:**
```text
Analyze the "Personal Profile" in the Project Knowledge.

Perform a Gap Analysis between his Current Skill Set vs. his Learning Goals.
Output a table showing: Current Skill Level, Required Skill Level, and the "Gap".
```

**Expected Output:** A table identifying gaps like "Python Syntax", "Pandas Dataframes", "Data Cleaning logic".

---

### STEP 2: Learning Path

**Prompt:**
```text
Based on the Gap Analysis above, create a sequential Learning Path.
Break this down into Phases, for each phase, list specific sub-skills he must master.
```

**Expected Output:** A structured list of phases and topics.

---

### STEP 3: Resource Curation

**Prompt:**
```text
Based on the Learning Path and the profile, curate a list of specific 

Suggest 3 specific courses, books, or documentation sites that fit this style.
```

**Expected Output:** A list of resources like "Automate the Boring Stuff", "Pandas Cookbook", etc.

---

### STEP 4: Weekly Schedule

**Prompt:**
```text
Based on the Resources selected and Ahmed's time constraints (3 hours/week mid-month, blackout during first 5 days), create a realistic 8-week study schedule.
Map specific resources to specific weeks.
Include "Buffer Weeks" for month-end close periods where no studying happens.
```

**Expected Output:** A calendar-like view of what to study when.

---

## Student Build (60 min)

**Task:** Manually chain all 4 steps of YOUR process in a single chat.
1. Prompt Step 1 → Get Output
2. Prompt Step 2 (referencing Step 1) → Get Output
3. Prompt Step 3 (referencing Step 2) → Get Output
4. Prompt Step 4 (referencing Step 3) → Get Output

**Discussion:** Did the AI lose context by Step 4? Did you have to repeat instructions?

**Transition to Session 4:** "Keeping the chain in your head is hard. We need a map—an SOP that holds the logic so you don't have to."
