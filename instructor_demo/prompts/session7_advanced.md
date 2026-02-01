# Session 7: Optimization & Advanced Engineering
## Instructor Demo Script

**Duration:** 60 min power tools + 45 min student optimization

---

## Part 1: The "Power Tools" (60 min)

### SETUP (say to class):
> "R-C-T-C works for most tasks. But sometimes you need more precision. These are the 'power tools' for when standard prompts aren't enough."

---

## Tool 1: Few-Shot Examples (15 min)

### THE PROBLEM:
> "The AI's tone is generic. It doesn't match your organization's style."

### THE FIX:
> "Give it 2-3 examples of PERFECT output. 'Write like THIS.'"

---

### DEMO: Generic vs Few-Shot

**Prompt WITHOUT Few-Shot:**
```
Write a milestone description for completing the pandas fundamentals module.
```

**Expected Output (Generic):**
```
Milestone: Successfully completed pandas fundamentals, demonstrating
proficiency in data manipulation and analysis techniques.
```

**Say to class:**
> "Technically correct. But bland. Let's show it what we actually want."

---

**Prompt WITH Few-Shot:**
```
Write a milestone description for completing the pandas fundamentals module.

Match this style (practical, specific, action-oriented):

EXAMPLE 1:
"Can open any Excel file and immediately filter it down to the 10 rows
that matter, without touching Excel."

EXAMPLE 2:
"Can answer 'What were last month's top 5 cost centers?' in 30 seconds
using 3 lines of Python instead of a 10-minute pivot table rebuild."

Now write the milestone for pandas fundamentals in this same style:
```

**Expected Output (Few-Shot):**
```
"Can load a messy GL export, clean it up, and have a summary table
ready before the coffee finishes brewing - all without opening Excel."
```

**TEACHING POINT:**
> "Same question. Different output quality. The examples TEACH the AI your style better than any description could."

---

### PRACTICE EXERCISE: Few-Shot Mini-Lab (10 min)

> "Take one of your Step outputs that felt 'generic'. Add 2 examples of what GOOD looks like in your organization. Re-run and compare."

---

## Tool 2: Chain of Thought (CoT) (15 min)

### THE PROBLEM:
> "The AI makes logic errors or jumps to conclusions without showing its work."

### THE FIX:
> "Force it to think step by step. 'Show your reasoning.'"

---

### DEMO: Logic Error Without CoT

**Scenario:** Ahmed asks about learning priority

**Prompt WITHOUT CoT:**
```
Should Ahmed learn data visualization (matplotlib/seaborn) as part of the
Month-End Close automation project?
```

**Expected Output (Wrong Jump):**
```
Yes, data visualization is important for presenting financial data.
Ahmed should add matplotlib and seaborn to the learning plan for
creating charts in the CFO reports.
```

**Say to class:**
> "This sounds reasonable but it's WRONG for Ahmed's specific goal. The CFO report uses Excel charts, not Python charts. The AI jumped to a conclusion without reasoning through it."

---

**Prompt WITH CoT:**
```
Should Ahmed learn data visualization (matplotlib/seaborn) as part of the
Month-End Close automation project?

Think step by step:
1. What is Ahmed's actual goal?
2. What does the current CFO report contain?
3. Would Python charts add value or just add scope?
4. What is the opportunity cost of learning visualization?

Then provide your recommendation.
```

**Expected Output (With Reasoning):**
```
Let me think through this step by step:

1. **Ahmed's actual goal:** Automate Month-End Close data consolidation.
   The goal is speed and accuracy in data processing, not presentation changes.

2. **Current CFO report contents:** The MBR deck uses Excel-formatted tables
   and likely existing Excel charts. The output Ahmed described is
   "summary tables for CFO review" - tables, not charts.

3. **Would Python charts add value?** The CFO already has a presentation
   format they expect. Changing to Python-generated charts would:
   - Require buy-in from CFO on new visual style
   - Add learning time (4-6 hours for matplotlib basics)
   - Create a new output format to maintain

4. **Opportunity cost:** Those 4-6 hours could be spent on:
   - Error handling in the consolidation script
   - Documentation for handoff
   - Testing edge cases

**Recommendation:** No. Data visualization is OUT OF SCOPE for this project.
Ahmed should focus on the consolidation automation first. If the CFO later
requests Python-generated charts, that's a separate project.
```

**TEACHING POINT:**
> "CoT caught the scope creep. By forcing reasoning, we got a better answer."

---

### PRACTICE EXERCISE: CoT Challenge (10 min)

**Scenario for students:**
```
Debug this prompt. The AI said "yes" but the answer should be "no":

"Should we automate the exception approval step in the procurement process?"

The AI said: "Yes, automation reduces delays and human error."

But: Exceptions over $50K require VP signature for audit compliance.

Use CoT to get the correct answer.
```

**Solution:**
```
Should we automate the exception approval step in the procurement process?

Think step by step:
1. What is an "exception" in this context?
2. What are the approval requirements for exceptions?
3. Are there legal/audit requirements for human signatures?
4. What is the risk of automating this step?

Then provide your recommendation.
```

---

## Tool 3: Tree of Thought / Parallel Option Generation (15 min)

### THE PROBLEM:
> "The AI gives you ONE answer, but you need to compare OPTIONS before deciding."

### THE FIX:
> "Ask it to generate multiple paths in parallel, then evaluate them."

---

### DEMO: Single Path vs Tree of Thought

**Prompt WITHOUT ToT:**
```
What resource should Ahmed use to learn pandas?
```

**Expected Output (Single Answer):**
```
Ahmed should use "Python for Excel" by Felix Zumstein. It's specifically
designed for Excel users transitioning to pandas.
```

**Say to class:**
> "This might be right. But how do we know it's the BEST option? What are the alternatives?"

---

**Prompt WITH ToT (Parallel Options):**
```
Generate 3 different resource paths for Ahmed to learn pandas.
For each path, include:
- Resources and estimated cost
- Pros specific to Ahmed's profile
- Cons specific to Ahmed's constraints
- Best suited for (scenario)

Then recommend which path Ahmed should take and why.
```

**Expected Output (Tree of Thought):**
```
## PATH A: Book-Based (Traditional)
**Resources:** "Python for Excel" by Felix Zumstein ($50)
**Pros:**
- Directly addresses Excel→Python transition
- Can work through at own pace
- Offline access during commute
**Cons:**
- No interactive feedback
- Cookbook style but still requires reading long passages
**Best for:** Self-motivated learners comfortable with books

## PATH B: Video-Based (Visual)
**Resources:**
- "pandas for Excel Users" (YouTube playlist, free)
- DataCamp pandas track ($29/month)
**Pros:**
- Visual demonstrations match Ahmed's Excel mental model
- Immediate "follow along" coding
- Free option available
**Cons:**
- DataCamp exercises can be abstract
- YouTube quality varies
**Best for:** Learners who prefer watching over reading

## PATH C: Project-Based (Hands-On)
**Resources:**
- "Automate the Boring Stuff" Ch. 12-13 (free online)
- Build Month-End Close script from week 1
**Pros:**
- Immediately applicable - learning BY building the actual project
- Free
- Matches "cookbook" preference (practical recipes)
**Cons:**
- Steeper learning curve initially
- May miss foundational concepts
**Best for:** Impatient learners who want results fast

---

## RECOMMENDATION: Path C (Project-Based), with Path A as reference

**Reasoning:**
1. Ahmed explicitly stated "If it doesn't help me close the books faster, I don't care."
2. Ahmed has LIMITED time (3 hrs/week) - can't afford abstract exercises
3. Ahmed's "cookbook" preference = learn by doing, not by reading theory
4. Path C costs $0, Path A book ($50) as backup reference
5. Ahmed's VBA experience means they already think procedurally

**Implementation:** Start building the Month-End Close script immediately,
using "Python for Excel" as a reference when stuck on specific syntax.
```

**TEACHING POINT:**
> "ToT gives you OPTIONS and REASONING. You can make an informed decision instead of trusting the first answer."

---

### PRACTICE EXERCISE: ToT Exercise (10 min)

> "For one decision point in your process, generate 3 parallel options. Compare them, then recommend one."

**Template:**
```
Generate 3 different approaches for [YOUR DECISION POINT].

For each approach:
- Description
- Pros for my context: [YOUR CONTEXT]
- Cons given my constraints: [YOUR CONSTRAINTS]
- Best suited for: [scenario]

Then recommend which approach to take and why.
```

---

## Part 2: Student Optimization (45 min)

### INSTRUCTIONS:

> "Take your packaged Skill from Session 5B. Apply ONE of these power tools to make it even better."

**Checklist:**
1. Identify which problem you have:
   - Generic tone/style? → **Use Few-Shot**
   - Logic errors/jumped conclusions? → **Use CoT**
   - Need to compare options? → **Use ToT**

2. Rewrite the prompt with the power tool

3. Run both versions (packaged Skill vs optimized)

4. Score with the Quality Rubric:

### A/B TEST QUALITY RUBRIC:

| Criteria | V1 (Packaged) | V2 (Optimized) |
|----------|---------------|----------------|
| **Accuracy:** Facts/data correct? | /5 | /5 |
| **Format:** Followed constraints? | /5 | /5 |
| **Tone:** Professional/on-brand? | /5 | /5 |
| **Completeness:** All inputs used? | /5 | /5 |
| **TOTAL** | /20 | /20 |

5. **Update `prompts.md`:** Record V2.0 with the optimization applied

---

## Summary: When to Use Each Tool

| Problem | Tool | Trigger Phrase |
|---------|------|----------------|
| Output is generic/bland | Few-Shot | "Match this style..." |
| Logic errors, jumped conclusions | Chain of Thought | "Think step by step..." |
| Need to compare options | Tree of Thought | "Generate 3 approaches..." |
| Output too long/unfocused | Constraints | "Maximum 200 words..." |
| Missing key information | Context refresh | "Given that [X, Y, Z]..." |

---

## Screenshot Moments:
1. [ ] Few-Shot: Generic vs styled output comparison
2. [ ] CoT: Wrong answer without reasoning vs correct answer with reasoning
3. [ ] ToT: Single recommendation vs 3 options comparison table
4. [ ] Quality Rubric A/B comparison

---

## Key Takeaway:

> "R-C-T-C is your everyday toolkit. These power tools are for precision work. Know when to use each one, and your outputs will be consistently excellent."
