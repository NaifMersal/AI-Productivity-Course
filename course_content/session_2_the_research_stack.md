# Session 2: The First Interaction – The Research Stack (10:00 – 10:45)

**Goal:** Stop "asking" and start "interrogating." Build a **Trust Layer** of grounded data before you generate a single word of content.

---

## 1. The New Workflow: Context before Content

In the "Search Mindset," you start with a blank box and ask a question. In the **AI-Native Mindset**, you never start with a blank page. You start with **Context**.

If you ask an LLM to "Write a report on the Saudi Fintech market," it will give you a generic, Wikipedia-style summary that could have been written in 2021.
If you **upload** the **Financial Sector Development Program Annual Report 2023** ([Download PDF](https://www.sama.gov.sa/en-US/Documents/Financial_Sector_Development_Program_Annual_Report-2023-EN.pdf)) and *then* ask, you get a highly specific, citation-backed analysis that an expert would trust.

### **The "Context First" Rule:**
1.  **Don't Ask:** "What are the trends in tourism?"
2.  **Upload:** *Ministry of Tourism - Hospitality Investor Report* ([Download PDF](https://cdn.mt.gov.sa/files/Hospitality-Investor.pdf))
3.  **Instruction:** "Based *only* on the uploaded report, summarize the visitor adoption rates for the Red Sea destinations vs. AlUla."

---

## 2. The Trust Layer: The Antidote to Hallucinations

Hallucinations happen when the AI doesn't know the answer but tries to please you by guessing.
The **Trust Layer** is the practice of forcing the AI to use *your* sources as its only truth.

### **Why this matters for Saudi Professionals:**
*   **Government Proposals:** You cannot afford to quote a "Vision 2030 target" that doesn't exist.
*   **Legal/Compliance:** Citations must point to actual articles in the Labor Law or Tax Code.
*   **Corporate Strategy:** Market numbers for the Petrochemical sector must match the latest Tadawul disclosures, not internet estimates.

**The Golden Rule:** *If it doesn't have a citation, it didn't happen.*


---

## 3. Tools in Action: Building Your Stack

We will look at three tools that solve the "Research Problem" in different ways.

### **A. NotebookLM (Google)**
*   **Best For:** Deep reading of massive documents (50+ pages).
*   **The Magic:** It creates a "Source Guide" solely from your documents. It won't look at the outside internet unless you ask it to.
*   **Saudi Scenario (Petrochemicals):**
    *   *Input:* Upload 5 different "Sustainability Reports" from major global competitors (Dow, BASF, etc.).
    *   *Prompt:* "Compare the 'Scope 3 Emission' targets of these 5 companies against our internal draft policy. Create a table showing gaps."
    *   *Bonus:* Generate an "Audio Overview" (Podcast) to listen to while driving to King Abdullah Financial District (KAFD).

### **B. Deep Research (Perplexity / ChatGPT Pro/ Google Gemini)**
*   **Best For:** Real-time synthesis of the live web.
*   **The Magic:** It reads 20-30 websites in seconds and footnotes every sentence.
*   **Saudi Scenario (Tourism & Hospitality):**
    *   *Prompt:* "Find the top 5 complaints mentioned in tourist reviews for 5-star hotels in Riyadh during 'Riyadh Season' 2024. Group them by category (Service, Traffic, Price). Cite the specific TripAdvisor or Booking.com review source."
    *   *Result:* "30% of reviews cited 'Valet Parking Delays' (Source: Booking.com, Review #42)." — *Actionable intel, not generic fluff.*

### **C. Project Knowledge (Claude Projects / ChatGPT Team)**
*   **Best For:** Long-term project memory.
*   **The Magic:** You upload the "Project Charter" once, and it remembers it forever.
*   **Saudi Scenario (Fintech/Startups):**
    *   *Context:* You are launching a new 'Buy Now, Pay Later' (BNPL) app.
    *   *Setup:* Upload the "SAMA BNPL Guidelines" ([Download PDF](https://sama.gov.sa/en-US/RulesInstructions/FinanceRules/BNPL_rules_en.pdf)) and your "Product One-Pager" into a **Claude Project** or **Custom GPT**.
    *   *Prompt:* "Does our proposed 'Late Fee' structure (Section 4 of Product Doc) comply with Article 7 of the SAMA Guidelines? Highlight specific risk clauses."

---

## 4. Activity: "The 10-Hour Research Task in 10 Minutes"

**Scenario:**
It is 10:00 AM. Your Department Head just sent you a 40-page PDF report titled *"Global Trends in Green Hydrogen 2025"* (use the real-world **IEA Global Hydrogen Review 2024** - [IEA Report Page](https://www.iea.org/reports/global-hydrogen-review-2024)).
They have a board meeting at 11:00 AM and need a **1-page Executive Summary** on how this affects your company’s strategy.
Old Way: Read frantically, highlight, panic-type. (Time: 2 hours).

**Your Task (10 Minutes):**

1.  **Select Your Tool:** Open **NotebookLM** (or use Claude/ChatGPT with file upload).
2.  **The Upload:** Drag and drop the complex PDF.
3.  **The "Interrogation" Prompt:**
    > "Act as a Strategy Consultant for a Saudi Energy company.
    > Based *strictly* on this report, outline the 3 biggest opportunities and 3 biggest risks for our market.
    > If the information is not in the report, state 'Not found in source' DO NOT hallucinate.
    > Include page references for every point.
    > Conclude with a 'Recommended Stance' for the board meeting."
4.  **The Polish:** Verify the citations. (Click the little numbers to check the source text).
5.  **The Flex (Optional):** Generate an "Audio Overview" and send the link to your manager saying: *"Here is the summary, and I also generated a 5-minute podcast version if you prefer to listen on your way to the meeting."*

> **Quick Instruction for the Activity:**
> For the **"10-Minute Research Task"**, download the **IEA Hydrogen Report** linked above. It is over 100 pages. Uploading this to NotebookLM and asking it to "Find the 3 biggest risks for a Saudi Energy company" will perfectly demonstrate the power of the tool, as it will have to synthesize data from multiple chapters instantly.

> **Instructor Note:** Ensure you have the PDFs downloaded locally before the session starts to avoid internet bandwidth issues.

---

## 5. Micro-Check: Live Quiz

1.  **Scenario:** You need to summarize a confidential internal HR investigation report.
    *   *Tool:* Is it Ok to use **NotebookLM** ?
2.  **Scenario:** You need to know the stock price of Aramco *right now*.
    *   *Tool:* **Perplexity/Google Gemini** (Live Web Access). NotebookLM cannot do this (it is grounded in your docs).
3.  **Scenario:** You are writing a novel and want the AI to remember your characters for 3 months.
    *   *Tool:* **Claude Project** (Long context window + Persistent Memory).
