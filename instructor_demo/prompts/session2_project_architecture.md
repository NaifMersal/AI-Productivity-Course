# Session 2: The Workbench (Project Architecture)
## Instructor Demo Script

**Duration:** 15 min setup + 20 min student build + 10 min validation

---

## Part 1: The "Lazy Manager" Philosophy

### SETUP (say to class):
> "In Session 1, we learned that 'More Context = Better Output'. But we also saw that providing context manually is exhausting.
>
> **The Goal:** Write the context ONCE, and never type it again. We do this with **Claude Projects**."

---

## Part 2: Building the "Context Brain"

### INSTRUCTOR DEMO (while students follow along):

1. **Create New Project** in Claude
   - Name: "Skill Acquisition Planner"
   - Description: "Automated coach for Ahmed"

2. **Upload "The C" (Context)**
   - Upload `personal_profile.md`
   - *Teaching Point:* "This file contains the 7 years of experience and the detailed restrictions. We just dumped 500 words of context into the brain without typing a single letter."

3. **Configure "The R" (Role)**
   - Open **Project Instructions**.
   - **Say:** "This is where we define the Global Role."

   ```
   **GLOBAL R-C-T-C Setup:**

   ROLE:
   You are a professional development coach specializing in skill acquisition for busy professionals.

   CONTEXT:
   - You have access to the learner's professional profile in the project knowledge
   - Always reference their current skill level, time constraints, and learning preferences

   BEHAVIOR:
   - Respect their time constraints and suggest realistic timelines
   ```

---

## Part 3: The Payoff (Automated RCTC)

### SETUP (say to class):
> "Now watch what happens. My Project knows the ROLE and has the CONTEXT. So my prompt can just be the TASK."

### PROMPT (The "Context-Rich" Version)
```
Create a Python learning plan for me.
```

### EXPECTED RESPONSE:
The AI will now ignore the generic "ask clarifying questions" behavior and immediately generate a tailored 4-week plan because you provided the specific **T** (Task Context) to complement the **R** and **C** in the Project.

**TEACHING POINT:**
> "We moved the R and C from the **Chat Box** (Temporary) to the **Project** (Permanent). This is how you scale."

---

## Part 4: Student Build
Students set up their own Business Process Projects now, uploading their sanitized docs and setting their Global RCTC instructions.
