# Session 2: The Science of Delegation (R-C-T-C) (10:00 – 11:30)

**Goal:** Master the art of "First-Shot Perfection." Stop treating AI like a slot machine (hoping for a good answer) and start treating it like a direct report (delegating with precision).

---

## 1. The Framework: R-C-T-C

Most people fail with AI because they **ask** instead of **delegate**.

| The "Lazy" Prompt (Bad) | The "Delegation" Prompt (Good) |
| :--- | :--- |
| "Write an email about the meeting." | **Act as** a Project Manager. **Given** these notes, **Draft** a recap email. **Ensure** you use bullet points. |
| *Result:* The AI guesses. It might be too casual, too long, or miss the point. | *Result:* The AI knows exactly *who* it is, *what* it knows, *what* to do, and *how* to do it. |

To get a perfect result, you must provide the four pillars of delegation:

1.  **Role:** Who is the AI? (A Senior Consultant? A Python Expert? An Angry Customer?)
2.  **Context:** What is the background? (The efficient "brain dump" concept).
3.  **Task:** What exactly do you need? (Be specific: "Draft a 200-word email").
4.  **Constraint:** What are the rules?
    *   *Formatting:* "Use a markdown table", "Use bold headers".
    *   *Tone:* "Professional but warm", "Strictly factual".
    *   *Behavior:* "If the notes are unclear, ask me clarifying questions." (**Crucial for accuracy**).

> **Formula:**
> "Act as a **[Role]**. Given the following **[Context]**, complete this **[Task]**. Follow these **[Constraints]**."

---

## 2. Instructor Demo: The "Client Relationship Assistant"

**The Story:** *(Based on the article [I Built My First Custom Gemini Gem in 10 Minutes](https://medium.com/@ConnectAIbiz/i-built-my-first-custom-gemini-gem-in-10-minutes-bdb52e522e1b))*
I once nearly lost an $18,000 deal because of seven words scribbled in a notebook: *"Follow up on the pricing stuff soon."*
Three days later, the client ("Lisa") emailed asking if I had forgotten her. I had messy notes, no memory of the specifics, and a 48-hour deadline.

**The Solution:**
Instead of panic-writing, I built a reliable system using R-C-T-C.

### **The Input (The Messy Reality):**
> *Meeting with Lisa from Acme Retail. Tuesday. She’s worried about lead times. Wants to know if we can ship by Q3. Pricing: she needs a 10% discount if they buy bulk. Mentioned her kid’s graduation is next week (send a card?). Action: send updated proposal by Friday.*

### **The R-C-T-C Prompt:**

*   **Role:** Act as my Senior Client Relationship Manager.
*   **Context:** I just had a call with a VIP client, Lisa. We are negotiating a large contract. I have pasted my raw, messy notes below.
*   **Task:** Draft a professional follow-up email to Lisa summarizing our conversation and confirming next steps.
*   **Constraint:**
    *   **Tone:** Warm but professional.
    *   **Structure:** Use clear headers (Summary, Decisions, Next Steps).
    *   **Action Items:** Highlight deadlines in **bold**.
    *   **Clarifications:** If any critical details are missing from my notes, add a section at the bottom called "Clarifications Needed."

### **The Result (AI Output):**
> **Subject:** Recap & Next Steps: Acme Retail & [Your Company] Partnership
>
> Hi Lisa,
>
> Great speaking with you on Tuesday. I wanted to summarize our discussion and confirm the plan to move forward.
>
> **Summary**
> We discussed your timeline concerns and pricing options for the bulk order.
>
> **Decisions & Agreements**
> *   **Timeline:** We are targeting a Q3 delivery to align with your launch.
> *   **Pricing:** We can approve a **10% discount** for the bulk order as requested.
>
> **Next Steps**
> *   **Action:** I will send the updated proposal with the discount applied by **this Friday**.
>
> **Clarifications Needed (Internal):**
> *   *You mentioned "send a card" for her son's graduation. Do you want me to draft a separate note for that, or include it here? (Included a brief PS below for now).*
>
> Best,
> [My Name]
>
> *P.S. Best of luck with your son's graduation next week! I hope it’s a wonderful celebration.*

---

## 3. Student Activity: The "Project Lead" Simulation (Part 1)

**Scenario:**
You are a **Project Lead** at a major Saudi entity (e.g., PIF Giga-project or Ministry).
You have just received urgency messy notes from a strategy session regarding the **"Global Green Hydrogen Report"**.
You need to send an urgent update to your **Director**, "Dr. Ahmed," who is heading into a strategy meeting at the Ministry of Energy.

**Your Goal:**
Write an R-C-T-C prompt to generate a **"Red Flag Report"** email.

**The "Messy" Context (Copy/Paste this into your prompt):**
> *Just finished reading the IEA report. Big issues. Europe is moving slower than expected on hydrogen imports. This affects our export strategy for 2030. We might need to look at Asian markets (Japan/Korea) instead. Also, tech costs are dropping... actually, wait, electrolyzer costs are UP by 10% due to inflation. Good for us? No, bad for us. Need to tell Dr. Ahmed we should pause the "Euro-Deal" for 2 weeks until we see the new policy. Meeting is in 1 hour. Keep it short.*

**Step-by-Step Task:**

1.  **Open Cloud/ChatGPT/Gemini.**
2.  **Apply R-C-T-C:**
    *   **Role:** Who should the AI be? (Strategic Advisor? Crisis Manager?)
    *   **Context:** Paste the "Messy Context" above.
    *   **Task:** Draft a high-priority email to Dr. Ahmed.
    *   **Constraint:**
        *   Tone: Direct, urgent, executive-level (Saudi professional standard).
        *   Format: Bullet points for "Key Risks" and "Recommendations."
        *   **Pro Tip:** Add the "Clarifications Needed" constraint. The context has a contradiction ("Good for us? No, bad for us")—see if the AI catches it!
3.  **Execute & Refine:** Run the prompt. Does it sound like *you*?

---

## 4. Micro-Check: Live Quiz

**Question 1:**
You ask the AI: *"Write a marketing post about our new coffee shop in Riyadh."*
Which element of R-C-T-C is missing?
*   A) Role
*   B) Context (What makes the shop special?)
*   C) Task
*   D) Constraint (Platform? Length?)
*   **Answer:** B, D (and arguably A). It's a "Zero-Shot" disaster.

**Question 2:**
In the "Lisa" example, why was the **Constraint** ("Include a personal note") so important?
*   A) It makes the email longer.
*   B) It builds the relationship and proves you were listening.
*   C) The AI needs more words to process.
*   **Answer:** B. AI is great at data, but *relationships* are human. You must delegate the "human touch" explicitly.

---

## 5. Coming Up Next: Building the "Brain"
Right now, you are typing this R-C-T-C prompt manually every time.
**In Session 3**, we will turn this prompt into a permanent **"Button"** (Gem/GPT) so you never have to type it again. You will correct it once, save it forever.
