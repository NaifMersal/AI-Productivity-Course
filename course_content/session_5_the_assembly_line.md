# Session 5: The Assembly Line (SOPs & Workflows) (15:15 – 16:30)

**Goal:** Turn your AI into a reliable "factory worker." Move from "Creative Writing" to "Data Processing" by using Standard Operating Procedures (SOPs).

---

## 1. The Reality: "Garbage In, Garbage Out"

In the previous sessions, we focused on **creative** or **strategic** tasks (Delegation, Research, specialized "Brains").
But 80% of our work isn't creative. It's **processing**.

*   Agendas -> Minutes.
*   Invoices -> Spreadsheets.
*   Field Notes -> Reports.

**The Problem:**
Most people treat AI like a chatty intern for these tasks.
*   *User:* "Here are some notes, make them look nice."
*   *AI:* "Sure! Here is a lovely summary..." (Misses 3 key dates, hallucinates a budget item, and formats it as a poem).

**The Friction (The "Copy-Paste Loop"):**
You spend 5 seconds pasting the data, and 10 minutes fixing the AI's mistakes.
If you have to check every single line, **the AI is not saving you time.**

---

## 2. The Solution: The Markdown SOP

To get **industrial-grade reliability**, we stop treating the AI like a person and start treating it like a **machine**.
We give it an **SOP (Standard Operating Procedure)** written in Markdown.

### **The "Assembly Line" Logic:**

1.  **Input Conveyor Belt:** Raw, messy data (emails, PDFs, WhatsApp voice notes).
2.  **The SOP (The Machine):** A strict set of rules that processes the data.
3.  **Output Conveyor Belt:** Clean, structured data (Tables).

---

## 3. Real-World Scenario: The "Expense Report" Nightmare

**Context:**
You are a Consultant working on a project between **Riyadh** and **Jeddah**. It is the end of the month.
Your Finance Department (and the ZATCA regulations/Fatoora) are strict.
You have **3 chaotic inputs** that you need to turn into a clean Excel table for your claim.

### **The 3 Chaotic Inputs:**

**Input 1: The Crumpled Receipt (Photo/OCR)**
> *Restaurant: Najd Village, Riyadh.*
> *Items: Kabsa (Chicken) x2, Jareesh, Vimto.*
> *Total: SAR 145.00*
> *Date: 25/10/2025*
> *VAT Number: 300012345600003*

**Input 2: The Forwarded Email (Flynas)**
> *From: Flynas Reservations*
> *Subject: Confirmation XY782*
> *Flight XY782: RUH to JED.*
> *Seat: 4A (Business).*
> *Price: SAR 1,250.00*
> *Date: Oct 26th.*

**Input 3: The WhatsApp Voice Note (Transcript)**
> *"Hey, forgot to log the transport. Taken a Careem from the hotel to the Ministry at 9 AM, that was 45 Riyals. Then an Uber to the airport, 105 Riyals. Oh, and I bought a coffee at the airport for 25 Riyals. All on the 26th."*

---

### **Student Activity: Build the SOP**

**Your Task:**
Write a prompt that takes these mixed inputs and outputs a **single, perfect CSV table** ready for Excel.

**The "Bad" Prompt (Do NOT do this):**
> "Here are my receipts, please make a table."

**The "SOP" Prompt (Do this):**
*(Copy-Paste into your AI)*

```markdown
**Role:** You are a Senior Accountant for a Saudi consulting firm.

**Goal:** Process raw expense data into a strict financial log.

**Input Data:**
[PASTE THE 3 INPUTS HERE]

**SOP (Standard Operating Procedure):**
1.  **Scan** the text for financial transactions.
2.  **Categorize** each item into one of these tags: [Meals], [Travel], [Transport], [Office Supplies].
3.  **Standardize** dates to YYYY-MM-DD format.
4.  **Convert** all currencies to SAR (if needed).
5.  **Output** ONLY a Markdown Table with these exact headers:
    | Date | Vendor | Category | Amount (SAR) | VAT (15%) | Notes |

**Constraints:**
- If VAT is not visible, assume it is included (Gross Amount / 1.15 = Net).
- For "Vendor", if unknown, write "Cash Expense".
- Do not chat. Just output the table.
```

---

## 4. The Output: The Fuel for Session 6

If you run the SOP above, the AI ignores the "chatty" parts of the WhatsApp note and the decorative text of the receipt. It gives you this:

| Date | Vendor | Category | Amount (SAR) | VAT (15%) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2025-10-25 | Najd Village | Meals | 145.00 | 18.91 | Team Dinner |
| 2025-10-26 | Flynas | Travel | 1,250.00 | 163.04 | Flight RUH-JED |
| 2025-10-26 | Careem | Transport | 45.00 | 5.87 | Hotel to Ministry |
| 2025-10-26 | Uber | Transport | 105.00 | 13.70 | Ministry to Airport |
| 2025-10-26 | Airport Cafe | Meals | 25.00 | 3.26 | Coffee |

**Why this matters:**
This isn't just a table. It is **Structured Data**.
In **Session 6 (The Data Factory)**, we will take this exact dataset and ask the AI:
*"Analyze my travel spend vs. meals for Q4"* or *"Visualize this data."*

**You cannot analyze chaos. You can only analyze structure.**

---

## 5. Micro-Check: Live Quiz

**Question:**
Your SOP keeps failing to capture the "VAT Number" from receipts. What should you add to the prompt?
1.  "Please try harder."
2.  "If you miss the VAT number, I will be sad."
3.  A specific step in the SOP: *"Example: Look for text starting with 'VAT' or 'Tax ID' and extract the 15-digit code."*

**Answer:** 3. Be specific. If the machine fails, update the code (the SOP).
