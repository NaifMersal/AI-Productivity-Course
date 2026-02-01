# SKILL ACQUISITION PLANNER - STANDARD OPERATING PROCEDURE (SOP)

## Process Overview
**Purpose:** Transform a vague "I want to learn X" request into a structured, actionable learning roadmap tailored to the learner's profile.

**Input:** Skill request + Learner profile
**Output:** Personalized, time-blocked learning roadmap with resources and milestones

---

## WORKFLOW DIAGRAM

```
INPUT: "I want to learn [SKILL] for [REASON] in [TIMEFRAME]"
                    ↓
┌─────────────────────────────────────────────────────────┐
│  STEP 1: SKILL ASSESSMENT & GAP ANALYSIS               │
│  ─────────────────────────────────────────────────────  │
│  • Review learner's current skill profile               │
│  • Identify target skill requirements                   │
│  • Map existing skills → transferable foundations       │
│  • Identify specific gaps to close                      │
│                                                         │
│  OUTPUT: Gap Analysis Table (prioritized skill gaps)    │
└─────────────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────┐
│  STEP 2: LEARNING PATH DESIGN                          │
│  ─────────────────────────────────────────────────────  │
│  • Decompose skill into sub-skills                      │
│  • Identify dependencies (what must be learned first)   │
│  • Define measurable milestones                         │
│  • Estimate time per sub-skill                          │
│                                                         │
│  INPUT: Gap Analysis Table from Step 1                  │
│  OUTPUT: Learning Path Structure (sequence + milestones)│
└─────────────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────┐
│  STEP 3: RESOURCE CURATION                             │
│  ─────────────────────────────────────────────────────  │
│  • Match resources to learning style preference         │
│  • Verify resources fit budget constraints              │
│  • Select mix: tutorials, books, practice projects      │
│  • Prioritize resources with immediate application      │
│                                                         │
│  INPUT: Learning Path + Learner Preferences             │
│  OUTPUT: Curated Resource List (by sub-skill)           │
└─────────────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────┐
│  STEP 4: SCHEDULE GENERATION                    │
│  ─────────────────────────────────────────────────────  │
│  • Map sub-skills to available time blocks              │
│  • Respect time constraints (busy periods, blackouts)   │
│  • Include practice/application time                    │
│  • Build in review checkpoints                          │
│                                                         │
│  INPUT: Resources + Time Constraints                    │
│  OUTPUT: Schedule                                      │
└─────────────────────────────────────────────────────────┘
                    ↓
         OUTPUT: COMPLETE LEARNING ROADMAP
         ─────────────────────────────────
         • Personalized to learner's profile
         • Time-blocked to fit constraints
         • Resourced within budget
         • Milestone-tracked for progress
```

---

## STEP DETAILS

### Step 1: Skill Assessment & Gap Analysis

**Trigger:** Learner submits skill request

**Process:**
1. Parse the skill request to understand the target outcome
2. Review learner's professional profile for:
   - Current skill level (novice/intermediate/expert)
   - Related existing skills that transfer
   - Past learning experiences
3. Define what "success" looks like for this skill
4. Create gap analysis comparing current → target state

**Output Format:**
| Gap Area | Current Level | Target Level | Priority | Transferable Skills |
|----------|---------------|--------------|----------|---------------------|
| [skill]  | [1-5]         | [1-5]        | H/M/L    | [related skills]    |

**Handoff to Step 2:** Gap Analysis Table

---

### Step 2: Learning Path Design

**Trigger:** Gap Analysis Table received from Step 1

**Process:**
1. Break down target skill into teachable sub-skills
2. Determine learning sequence (prerequisites first)
3. Estimate realistic time for each sub-skill based on:
   - Gap size (current vs target level)
   - Learner's available time
   - Complexity of the sub-skill
4. Define measurable milestones (what can they DO after each sub-skill?)

**Output Format:**
```
LEARNING SEQUENCE:
1. [Sub-skill A] (Prerequisite: None) - Est. X hours
   Milestone: Can do [specific task]

2. [Sub-skill B] (Prerequisite: A) - Est. Y hours
   Milestone: Can do [specific task]

3. [Sub-skill C] (Prerequisite: A, B) - Est. Z hours
   Milestone: Can do [specific task]
```

**Handoff to Step 3:** Learning Path Structure

---

### Step 3: Resource Curation

**Trigger:** Learning Path Structure received from Step 2

**Process:**
1. For each sub-skill, identify resource types:
   - Tutorials (video/text)
   - Books/documentation
   - Practice exercises
   - Real-world projects
2. Filter by learner preferences:
   - Learning style (visual, reading, hands-on)
   - Preferred format (cookbook vs theoretical)
3. Verify budget constraints
4. Prioritize resources that allow immediate application

**Output Format:**
| Sub-skill | Resource | Type | Cost | Match to Style |
|-----------|----------|------|------|----------------|
| [skill]   | [name]   | [type]| [$] | [high/med/low] |

**Handoff to Step 4:** Curated Resource List

---

### Step 4: Weekly Schedule Generation

**Trigger:** Curated Resource List received from Step 3

**Process:**
1. Map available time slots from learner profile
2. Identify blackout periods (busy weeks, deadlines)
3. Allocate sub-skills to weeks based on:
   - Time available
   - Logical learning sequence
   - Buffer for practice/review
4. Include milestone checkpoints

**Output Format:**
```
WEEK 1: [Date Range]
- Focus: [Sub-skill]
- Time: [X hours]
- Resources: [List]
- Milestone: [What they can do by end of week]
- Practice Task: [Specific exercise]

WEEK 2: [Date Range]
...
```

**Final Output:** Complete Learning Roadmap

---

## DECISION POINTS

### If learner's goal is unclear:
→ Return to Step 1, ask clarifying questions before proceeding

### If available time is insufficient for skill complexity:
→ In Step 2, scope down to "minimum viable skill" or extend timeline

### If budget is insufficient for recommended resources:
→ In Step 3, prioritize free resources, adjust expectations

### If learner has no transferable skills:
→ In Step 1, add prerequisite sub-skills to the path

---

## QUALITY CHECKLIST

Before delivering final roadmap, verify:
- [ ] Every sub-skill has a measurable milestone
- [ ] Total time fits within learner's available hours
- [ ] Resources match learner's preferred style
- [ ] Total cost is within budget
- [ ] Blackout periods are respected
- [ ] Sequence respects prerequisites
- [ ] Final outcome matches original request
