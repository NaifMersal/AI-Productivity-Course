# Session 5B: Operational Readiness - Skill Packaging
## Instructor Demo Script

**Duration:** 45 min skill packaging + 30 min version control + 30 min final check

---

## Phase 1: Packaging as a Claude Skill (45 min)

### SETUP (say to class):
> "You've built a working workflow. Now let's package it so ANYONE on your team can use it - even if they weren't in this workshop."

### CONCEPT: What is a Claude Skill?
> "A Skill is a reusable, shareable prompt template. Think of it as a 'function' that takes inputs and produces consistent outputs."

---

### DEMO: Packaging the Skill Planner

**Say to class:**
> "I'm going to take everything we built - the SOP, the prompts, the chain - and package it into a single, reusable Skill."

---

### THE SKILL STRUCTURE:

```
---
name: skill-acquisition-planner
description: Creates personalized learning roadmaps when users request help learning a new skill, building competency, or creating professional development plans. Use when someone says they want to learn something or improve in an area, especially when they mention time constraints, career goals, or specific outcomes they want to achieve.
---

# Skill Acquisition Planner

Create structured, personalized learning roadmaps that transform vague "I want to learn X" requests into actionable plans.

## Approach

When helping someone learn a skill:

1. **Understand context first** - Ask about their current level, why they want this skill, timeline, available time per week, budget constraints, and learning style preferences (hands-on vs. theoretical, video vs. reading, etc.)

2. **Assess gaps** - Identify what they already know that transfers, what's truly new, and what's most critical for their stated goal

3. **Design the path** - Break the skill into sub-skills with clear prerequisites, estimate time for each, and identify measurable milestones (not just "understand X" but "can do X")

4. **Curate resources** - Match resources to their learning style and budget, prioritize "cookbook" style resources for practical learners, prefer free/affordable options unless they specify otherwise

5. **Create schedule** - Distribute learning across their available time, respect stated constraints (blackout periods, busy seasons), build in practice time and review cycles

## Key Principles

- **Connect to their goal** - Every recommendation should trace back to why they're learning this
- **Respect constraints** - Don't create plans that require 20 hours/week if they have 5
- **Make it measurable** - Each milestone should be testable ("can build X" not "understand Y")
- **Prioritize ruthlessly** - Focus on what gets them to their goal fastest, flag nice-to-haves separately

## When NOT to use this approach

- For academic research or deep theoretical study (different structure needed)
- When they just want resource recommendations without a full plan
- For skills requiring in-person instruction or specialized equipment you can't account for
```



I want to learn SQL for querying our data warehouse in 6 weeks.

My profile is in the project knowledge as personal_profile.md.

Please create a complete learning roadmap following your 4-step process.


**Say to class:**
> "Notice: I didn't have to explain the process. The Skill KNOWS the process. Anyone on my team can now invoke this Skill and get consistent results."

---

## Phase 2: Version Control (30 min)

### SETUP (say to class):
> "Prompts are CODE. They degrade if changed randomly. Let's version control them."

---

### DEMO: Create `prompts.md` Library

**In your Project, create a new file:**

```markdown
# PROMPT VERSION LIBRARY

## Document Info
- **Project:** Skill Acquisition Planner
- **Last Updated:** [DATE]
- **Owner:** [Your Name]

---

## VERSION LOG

| Version | Date | Change | Author |
|---------|------|--------|--------|
| v1.0 | [Day 1] | Initial 4-step workflow | [Name] |
| v1.1 | [Day 2] | Added Safety Check | [Name] |
| v2.0 | [Day 2] | Packaged as Skill | [Name] |

---

## GOLDEN PROMPTS

### PROMPT 1: Full Workflow Invocation (v2.0)

```
I want to learn [SKILL] for [REASON] in [TIMEFRAME].

My profile is in the project knowledge.

Please create a complete learning roadmap following your 4-step process:
1. Skill Assessment & Gap Analysis
2. Learning Path Design
3. Resource Curation
4. Weekly Schedule Generation

Deliver each step's output before proceeding to the next.
```

**Notes:**
- v2.0 assumes profile is already in project knowledge

---

### PROMPT 2: Quick Gap Analysis Only (v1.0)

```
Based on my profile, what are the top 3 skill gaps I should address to achieve [GOAL]?

Format as a prioritized list with:
- Gap description
- Current vs target level
- Estimated learning time
```

**Notes:**
- Use when learner just needs assessment, not full roadmap
- Quick win prompt for initial consultations

---

### PROMPT 3: Resource Recommendation (v1.0)

```
I need to learn [SPECIFIC_SKILL].

Given my learning preferences:
- Style: [cookbook/theoretical/visual]
- Budget: [amount]
- Time per week: [hours]

Recommend 3 resources, explaining why each fits my constraints.
```

**Notes:**
- Standalone prompt when learner already knows what to learn
- Good for resource refresh or alternatives
```

---

### VERSION CONTROL BEST PRACTICES:

| Practice | Why |
|----------|-----|
| Date every change | Know when issues were introduced |
| Describe what changed | Future you will forget why |
| Keep old versions | Rollback if new version fails |
| Test before promoting | v1.1-beta before v1.1 |
| One change per version | Easier debugging |

---

## Phase 3: Final Logic Check (30 min)

### ACTIVITY:

> "Run your full process end-to-end with ALL improvements:
> - SOP uploaded
> - Safety checks in place
> - Skill packaged"

### CHECKLIST:

**Before running:**
- [ ] SOP is in Project Knowledge
- [ ] Profile/context docs are in Project Knowledge
- [ ] System prompt is set in Project Instructions
- [ ] You have the invocation template ready

**During run:**
- [ ] Step 1 output matches expected format
- [ ] Step 2 references Step 1 output correctly
- [ ] Step 3 references Step 2 output correctly
- [ ] Step 4 produces complete schedule

**After run:**
- [ ] Final output achieves the original goal
- [ ] No constraints were violated
- [ ] Output is usable without editing

---

## Screenshot Moments:
1. [ ] Skill structure document
2. [ ] Project Instructions with System Prompt
3. [ ] `prompts.md` version library
4. [ ] Full workflow execution (start to finish)
5. [ ] Final output - the complete learning roadmap

---

## Student Activity: Package YOUR Skill

**Instructions:**

1. **Define your Skill:**
   - Name (action-oriented)
   - Description (1-2 sentences)
   - Trigger (when to use)

2. **Write the System Prompt:**
   - Combine your R-C-T-C elements
   - Include your SOP reference
   - Add output standards

3. **Define Input Variables:**
   - What does the user provide?
   - What are the placeholders?

4. **Create the Invocation Template:**
   - The "magic words" that trigger the full workflow

5. **Document in `prompts.md`:**
   - Add version number
   - Record changes from Day 1

6. **Test with a colleague:**
   - Can they invoke your Skill successfully?
   - Does the output meet your quality checklist?

---

## Transition to Session 6:

> "Your Skill works. But does it work SAFELY? Let's add the guardrails."

---

## Key Takeaway:

> "A Skill is a prompt that anyone can use. Version control means you can improve it without breaking it. This is how you scale AI assistance across a team."
