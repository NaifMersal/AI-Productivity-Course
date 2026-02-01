# Session 1: The Science of Prompting (R-C-T-C)
## Instructor Demo Script

**Duration:** 10 min bad demo + 20 min framework + 15 min student practice

---

## Part 1: The "Bad Delegation" (The Trap)

### SETUP (say to class):
> "Most people treat AI like a search engine. They ask a question and hope for a good answer. We call this 'The Slot Machine' approach. Let's see why it fails."

### PROMPT 1 - The Bad Delegation
```
Create a learning plan to become fluent in Python.
```

### EXPECTED RESPONSE:
Claude will generate a generic 3-6 month plan covering:
- Basic syntax
- Control flow
- Functions/OOP
- Libraries

**TEACHING POINT:**
> "This is technically correct but completely useless for a busy professional. It doesn't know WHO you are, WHAT you need, or HOW FAST you need it. We delegated the **Task**, but we forgot the **Manager**."

---

## Part 2: The Structured Solution (R-C-T-C)

### SETUP (say to class):
> "To get consultant-level output, we need to structure our request. We use the R-C-T-C Framework."

### THE FRAMEWORK:
| Letter | Meaning | Question to Ask |
|--------|---------|-----------------|
| **R** | Role | Who should the AI be? |
| **C** | Context | What background info does it need? |
| **T** | Task | What exactly should it do? |
| **C** | Constraint | What are the rules/limits? |

### DEMO: Building the Perfect Prompt
**Say:** "Let's rewrite that bad prompt using R-C-T-C."

### PROMPT 2 - The R-C-T-C Version
```
**ROLE:**
You are a professional development coach who specializes in helping finance professionals learn technical skills. You prefer practical "cookbook" styles over theory.

**CONTEXT:**
The learner is Ahmed, a Senior Financial Analyst.
- Goal: Automate Month-End Close in Excel
- availability: 3 hours/week
- Current Skills: Expert Excel/VBA, Novice Python

**TASK:**
Create an 8-week learning roadmap to take Ahmed from novice to automating his first report.

**CONSTRAINTS:**
- No abstract exercises; only practical recipes.
- Respect the 3 hr/week limit.
```

### EXPECTED RESPONSE:
A highly personalized, actionable plan that fits Ahmed's life perfectly.

---

## Part 3: The Friction (Transition to Session 2)

### ASK THE CLASS:
> "This result is amazing. But be honest — who wants to type that 200-word prompt every time you have a question?"


> "The R-C-T-C framework is powerful, but it's **heavy**. In Session 2, we will build an architecture that handles the 'R' and 'C' for us automatically, so you can just focus on the 'T'."

---

## Screenshot Moments
1. [ ] Bad Prompt result
2. [ ] R-C-T-C Table Slide
3. [ ] Good R-C-T-C Prompt result
