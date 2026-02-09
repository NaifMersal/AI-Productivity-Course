# Session 5: Advanced Prompt Engineering (15:15 – 16:30)

## **Goal**
Move beyond simple "input-output" prompts. Teach the model to *reason* (System 2 thinking) before answering.
This drastically reduces errors and "hallucinations" in complex tasks.

---

## **1. The "Fast vs. Slow" Problem**
*   **System 1 (Fast):** Intuitive, quick, prone to errors. (e.g., "Write a poem.")
*   **System 2 (Slow):** Deliberate, logical, step-by-step. (e.g., "Solve this riddle.")

**The Rule:** Complex tasks require System 2.

---

## **Technique 1: Chain of Thought (CoT)**
**Concept:** Adding the phrase **"Let's think step by step"** forces the AI to check its own logic. This catches errors before they happen.

### **Example: "The Lunch Break" (Scheduling)**
**Context:** You are building a schedule.
**The Prompt:**
> "I have a 2-hour meeting starting at 11:00 AM.
> **Constraint:** We must pause for a 30-minute lunch break at 12:00 PM.
> When does the meeting end?"

**❌ Standard Output (System 1 Failure):**
> "The meeting starts at 11:00 AM and lasts for 2 hours, so it ends at **1:00 PM**."
> *(The AI sees "2 hours" and "11:00" and does simple math: 11+2=13. It ignores the break logic.)*

**✅ CoT Prompt (System 2 Success):**
> "I have a 2-hour meeting starting at 11:00 AM.
> **Constraint:** We must pause for a 30-minute lunch break at 12:00 PM.
> When does the meeting end? **Think step-by-step.**"

**AI Response:**
> "1. The meeting starts at 11:00 AM.
> 2. First hour: 11:00 to 12:00.
> 3. **Pause for Lunch:** 12:00 to 12:30.
> 4. Second hour: 12:30 to 1:30 PM.
> **Final Answer:** The meeting ends at 1:30 PM."

---

## **Technique 2: Tree of Thoughts (ToT)**
**Concept:** Simulate a "Team Meeting" in the AI's head to explore different perspectives before deciding.

### **Example: "The Angry Client" (Strategy)**
**Context:** A major client is furious about a missed deadline. You need to write an email response.
**Task:** Decide the best tone and strategy.

**The "Experts" Prompt:**
> "Imagine three experts debating the best response:
> 1.  **The Empathetic Support Lead:** Wants to apologize profusely and offer a refund.
> 2.  **The Pragmatic Project Manager:** Wants to explain *why* it happened and propose a new timeline.
> 3.  **The Legal Advisor:** Wants to admit nothing to avoid liability.
>
> **Step 1:** Have them debate the pros/cons of each approach.
> **Step 2:** Synthesize a final response that balances empathy with professional boundaries."

---

## **Technique 3: Self-Consistency**
**Concept:** Ask the AI to do the work 3 times. If 3/3 match, trust it. If not, flag it. Best for accurate data extraction.

### **Example: " The Invoice Checker" (Accuracy)**
**Context:** You have a messy PDF invoice where the handwriting is hard to read.
**Task:** Verify if the 'Total Amount' matches the sum of the line items.

**The Prompt:**
> "Extract the line items and sum them up.
> Do this calculation 3 separate times independently.
> - Run 1 Result: [Sum]
> - Run 2 Result: [Sum]
> - Run 3 Result: [Sum]
>
> If all three match, output 'Verified'. If there is any difference, output 'Manual Review Needed'."

---

## **Activity: "The Team Offsite" (20 Minutes)**
**Scenario:** Scheduling a 1-Day Team Retreat.
**Objective:** Create an agenda that fits everyone's constraints.

**The Constraints:**
*   Start at 9:00 AM.
*   Must include a 2-hour "Strategy Workshop".
*   Must include Salat Al-Dhuhr (20 mins).
*   Lunch (1 hour) must be *after* Salat.
*   The CEO can only attend for 1 hour between 11:00 and 13:00.

**Activity Task:**
Use **Chain of Thought** to build a schedule where the 'Strategy Workshop' overlaps with the CEO's availability, without missing Prayer or Lunch.

---

## **Micro-Check: Quick Quiz**
1.  **Logic/Math Problem?** -> Use *Chain of Thought*.
2.  **Brainstorming/Strategy?** -> Use *Tree of Thoughts*.
3.  **Data Verification?** -> Use *Self-Consistency*.
