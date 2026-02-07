# Session 1: The Science of Delegation (R-C-T-C)

**Duration:** 1.5 Hours
**Goal:** Shift mindset from "Search Engine" to "Manager" using the R-C-T-C Framework.

---

## 09:00 - Opening: The Setup & Safety First (30 min)

### 1. Operations & Logistics
*   Welcome & Introductions.
*   **Tech Check:** Everyone logged into Claude?

### 2. Data Safety Breakdown (The "Newspaper Test")
**Instructor Script:**
> "Before we type a single word, we need to agree on safety. We are managers. We don't leak trade secrets."

*   **The Rule:** "Don't put anything in the chat you wouldn't want on the front page of the New York Times."
*   **The Action:**
    *   Never upload raw PII (Personally Identifiable Information).
    *   Never upload API keys or passwords.
    *   *Activity:* "Take 2 minutes. Look at the documents you brought. Are they clean? If not, redact them now."

### 3. The "Manager's Mindset"
**Instructor Script:**
> "Stop thinking of Claude as a computer. Think of it as a brilliant but literal-minded junior intern. It works at 1,000x speed, but it has no common sense. If you give vague instructions, you get vague results. We are here to learn **Delegation**."

---

## 09:30 - Part 0: Primer - How LLMs "Think" (15 min)

**Concept:** Prediction vs. Knowledge.
*   **Not a Database:** The AI is a statistical machine, not a fact retriever. It predicts the next likely word based on training; it doesn't "look up" facts.
*   **Transition:** "Since it doesn't know facts, YOU must be the Manager."

### 🧠 Deep Dive: The "Prediction Machine"
**The "Why":**
Understanding that LLMs are "Predictors" not "Knowers" saves you from the most dangerous risk: **Hallucination**. When an LLM doesn't know an answer, it doesn't say "I don't know"—it predicts what a confident answer *would* look like.

**Real-World Analogy:**
Think of your phone's Autocomplete, but with a PhD. If you type "The capital of France is...", it completes "Paris" because that is statistically probable. If you type "The secret ingredient in my grandmother's soup is...", it will invent an ingredient because it's completing the pattern, not accessing your grandmother's recipe book.

**Manager's Challenge:**
*   **Validation:** Never trust an unverified fact from an LLM.
*   **Verification:** Always ask for sources or checking against your own data.


---

## 09:45 - Part 1: The Trap (Bad Delegation) (10 min)

**Activity:** "The Bad Delegation" (Vague prompt -> Vague result).
*   **Concept:** AI needs a Manager, not just a requester.
*   **The Setup:** "Most people treat AI like a search engine. They ask a question and hope for a good answer. We call this 'The Slot Machine' approach."
*   **Demo (Projected):**
    *   *Bad Prompt:* `Create a learning plan to become fluent in Python.`
    *   *Result:* Generic 3-6 month plan covering syntax, loops, and theory. Technically correct, but useless for a busy professional.
*   **Key Learning:**
    *   **Garbage In, Garbage Out:** The model can only reason from the context you give it.
    *   **Anchoring:** LLMs tend to anchor on early assumptions. If a conversation starts vague, the ambiguity compounds. Restarting with a clear "manager-style" prompt is better than incremental corrections.

### 🧠 Deep Dive: The Cost of Ambiguity
**The "Why":**
In business, ambiguity costs money. A vague email leads to a 10-email thread. A vague prompt leads to 20 minutes of "prompt engineering" (tweaking). It is faster to spend 2 minutes writing a clear prompt than 20 minutes fixing a bad one.

**Real-World Analogy:**
You order a "Sandwich".
*   **The Result:** You get Tuna on Rye. You hate Tuna.
*   **The Fix:** You say "No, not Tuna." You get Ham. You wanted Turkey.
*   **The Manager's Approach:** "I want a Turkey Club on white toast, mayo on the side." One distinct, clear order.

**Your Manager's Challenge:**
*   Look at the "Bad Prompt" you just wrote.
*   **I Like:** That you started with a verb (Create, Write, Do).
*   **I Wish:** You had specified the *format* of the output (Table? Email? Bullet points?).
*   **I Wonder:** If you gave Claude a specific persona/role, would the tone improve?

---

## 09:55 - Part 2: The Framework (R-C-T-C) (45 min)

**Concept:** Reliability comes from Structure.

### The R-C-T-C Framework
| Letter | Meaning | Question to Ask |
|--------|---------|-----------------|
| **R** | **Role** | Who is the AI? (Contextual anchor) |
| **C** | **Context** | Background info, data, "The Why". |
| **T** | **Task** | The specific action. "The What". |
| **C** | **Constraint** | Format, tone, limits. "The How". |

### Instructor Demo: Building the Perfect Prompt
**Scenario:** Personal Skill Acquisition Planner for "Ahmed".

**The Prompt Build:**
*   **Role:** "You are a professional development coach who specializes in helping finance professionals learn technical skills. You prefer practical 'cookbook' styles over theory."
*   **Context:**
    *   Learner: Ahmed, Senior Financial Analyst.
    *   Goal: Automate Month-End Close.
    *   Availability: 3 hours/week.
    *   Current Skills: Expert Excel/VBA, Novice Python.
*   **Task:** "Create an 8-week learning roadmap to take Ahmed from novice to automating his first report."
*   **Constraint:** "No abstract exercises; only practical recipes. Respect the 3 hr/week limit."

**Student Activity:**
1.  Open the "bad prompt" you wrote earlier.
2.  Rewrite it using R-C-T-C.
3.  Run it.
4.  Compare the difference.

---

## 10:40 - Part 3: The Friction (Transition) (20 min)

**Discussion:**
*   "That worked better, right? The output is tailored and usable."
*   "But looking at your screens... who wants to type that 300-word paragraph every single time you need a report?"

**The Problem:**
*   Quality requires context.
*   Context is heavy.
*   Typing the "R" and "C" every time is unsustainable friction.

**Transition:** "We need an architecture to handle the 'R' and 'C' automatically. In the next session, we'll build a machine to carry that weight for us."

---

## ☕ Break (15 Minutes)
