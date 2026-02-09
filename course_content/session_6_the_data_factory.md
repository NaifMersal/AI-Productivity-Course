# Session 6: The Data Factory (Data Enrichment)

**Duration:** 09:00 – 10:45  
**Goal:** Master data-driven storytelling and transform raw data into executive intelligence.

---

## 1. Introduction: The Data Refinery

> *"Data is the new oil."* — Clive Humby

We hear this quote constantly in the Kingdom. But here is the reality: **Crude oil is useless.** You cannot put crude oil in your car; it will destroy the engine. It must be **refined** into fuel.

The same applies to your data.
*   **Raw Data (Crude Oil):** Messy receipts, bank exports with codes like `UBER*TRIP-2847`, and inconsistencies.
*   **Enriched Data (Fuel):** Structured, categorized, and compliant data ready for decision-making.

In this session, we build **The Data Factory**. You will move from being a "Data Entry Clerk" to a "Data Refinery Manager."

---

## 2. The Workflow Pattern: "The Analyst"

To build this factory, we adopt the **"Analyst"** persona. This is not about asking the AI to "chat." It is about asking the AI to **process**.

**The Cycle:**
1.  **Upload:** Feed the raw CSV/Excel file.
2.  **Enrich (The 3 Layers):** Clean, Categorize, and Audit.
3.  **Visualize:** Turn rows and columns into insights.

---

## 3. Data Enrichment: The 3 Layers

We will use the **Financial Data** we prepared in Session 5 (The Assembly Line). However, even "clean" data from an export often hides dirty secrets. We apply three layers of intelligence to fix this.

### Layer 1: The "Smart Categorizer" (Context Awareness)
**Theory:** Raw bank descriptions are often vague. A rule-based system struggles with context, but an LLM understands it.

*   **Scenario:** You see a charge for "Jarir Bookstore."
    *   *Old Way:* Rule says "Jarir = Books."
    *   *AI Way:* Look at the amount.
        *   SAR 45? -> **Office Supplies** (Pens/Notebooks).
        *   SAR 4,500? -> **IT Assets** (Laptop/iPad).
*   **Example:**
    *   **"Al Baik"** -> Meals & Entertainment.
    *   **"Saudi Airlines"** -> Travel.
    *   **"STC Pay"** -> Utilities or Petty Cash Transfer (needs context).

### Layer 2: The "Merchant Cleaner" (Normalization)
**Theory:** Executives want to see "How much did we spend on Uber?" They do *not* want to see 50 lines for `Uber * Trip 882`, `Uber * Trip 991`, etc.

*   **The Fix:** We tell the AI to "Normalize" text strings.
    *   `Uber * Trip 284J` -> **Uber**
    *   `HungerStation * BurgerKi` -> **HungerStation**
    *   `Flynas XY123` -> **Flynas**

### Layer 3: The "Policy Police" (Anomaly Detection)
**Theory:** This is your compliance layer. We teach the AI the "Rules of the Road" for your organization.

*   **Anomalies to Flag:**
    *   **The "Weekend" Trap:** Flag any "Business Lunch" that happened on a **Friday or Saturday**.
    *   **The "VAT" Gap:** Flag any transaction where the listed VAT is not exactly 15% of the base amount (identifying mathematical errors or non-compliant invoices).
    *   **The "Duplicate" Double-Dip:** Flag identical amounts to the same vendor on the same day (e.g., scanning the same receipt twice).

---

## 4. Activity: The "Expense Analysis Dashboard"

**Scenario:**
You are a Senior Analyst at a fast-growing Saudi logistics company. Your CFO has asked for an immediate "Q4 Spend Analysis" and a "Compliance Report" for the upcoming board meeting.

**The Assets:**
*   You have the `expenses_export.csv` file from Session 5.

**The Task:**
Use your AI (ChatGPT Plus / Claude / Gemini Advanced) to act as **The Data Factory**. You must turn this CSV into a Dashboard and a "Naughty List" of policy violations.

### Step 1: The "Refinery" Prompt (Copy & Paste)

Upload your CSV file and paste this prompt. Note how we explicitly define the **3 Layers**.

> **Role:** You are a Senior Financial Analyst for a Saudi corporation.
>
> **Context:** I have uploaded a raw expense export (`expenses_export.csv`). The data is messy and needs enrichment before we can visualize it.
>
> **Action:** Please process this data through the following 3 layers and output a **single cleaned table**:
>
> **Layer 1: Merchant Normalization**
> *   Remove transaction codes from vendor names (e.g., change "Uber * Trip 284J" to "Uber").
> *   Standardize naming (e.g., "Jarir Book" and "Jarir Bookstore" should both be "Jarir").
>
> **Layer 2: Smart Categorization**
> *   Ensure every row has a Category.
> *   If "Category" is empty or "Misc", infer it from the Vendor (e.g., "Al Baik" = Meals, "Flynas" = Travel).
>
> **Layer 3: The Policy Police (Flagging)**
> *   Create a new column called **"Compliance Flag"**.
> *   Mark as **"RED FLAG"** if:
>     1.  The transaction date falls on a **Friday or Saturday** (Weekend in Saudi Arabia).
>     2.  The Category is "Meals" but the Amount is > 500 SAR (Over policy limit).
>     3.  Possible duplicate (Same Vendor, Same Amount, Same Date).
> *   Mark as **"OK"** if no issues found.
>
> **Output:** Display the first 10 rows of the Enriched Table.

### Step 2: The "Executive" Visualizations

Once the AI confirms the data is clean, ask for the visuals.

**Prompt:**
> "Great. Now, act as a Data Storyteller. Generate the following charts for the Board Presentation:
>
> 1.  **Total Spend by Category (Bar Chart):** Sort high to low.
> 2.  **The 'Weekend Warrior' Report:** A filtered table showing ONLY the rows flagged as 'RED FLAG'.
> 3.  **VAT Analysis:** Calculate the total VAT paid and verify if it matches 15% of the total Net Amount."

### Step 3: The "Interview"

Don't just look at the charts. **Talk** to your data.
*   *"What is our biggest single expense vendor?"*
*   *"If we eliminated all 'Meals' expenses on weekends, how much would we save?"*
*   *"Draft a polite email to the employees on the 'Red Flag' list asking them to justify these weekend expenses."*

---

## 5. Course Material: Sample "Naughty List"

*Instructor Note: Show this example of what the AI should catch.*

| Date | Vendor | Category | Amount | Compliance Flag | Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2025-11-21 (Fri) | Starbucks | Meals | 69.37 | **RED FLAG** | Weekend Expense |
| 2025-10-15 | Extra Stores | Office Supplies | 2,400.00 | **RED FLAG** | Duplicate Transaction (Match found) |
| 2025-10-01 | Uber | Transport | 45.00 | OK | - |

---

## 6. Micro-Check (Quiz)

**Question:** Why do we ask the AI to "Normalize" vendor names before creating a chart?

A) To make the font size consistent.
B) To ensure "Uber" and "Uber Trip" are counted as the same vendor, preventing fragmented data.
C) To remove VAT calculations.

**Answer:** **B**. Consolidation is key to accurate reporting.
