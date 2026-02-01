# AHMED ALI: REALISTIC 8-WEEK PYTHON + PANDAS STUDY SCHEDULE
**Start Date:** February 3, 2026  
**End Date:** March 30, 2026  
**Study Cadence:** 3 hours/week (typically Wed 2–5 PM)  
**Blackout Periods:** Days 1–5 of each month (Month-End Close)  

---

## CALENDAR OVERVIEW (8 Weeks)

```
FEBRUARY 2026
SUN  MON  TUE  WED  THU  FRI  SAT
                                1
 2    3    4    5    6    7    8    ← WEEK 1: PHASE 1 START (Feb 3)
 9   10   11   12   13   14   15    ← WEEK 2: PHASE 1 (NO BLACKOUT - mid-month buffer)
16   17   18   19   20   21   22    ← WEEK 3: BUFFER WEEK (Feb 1-5 close happened)
23   24   25   26   27   28        ← WEEK 3.5: CATCH-UP / PHASE 2 START (late Feb)

MARCH 2026
SUN  MON  TUE  WED  THU  FRI  SAT
                                1    ← BLACKOUT BEGINS (Mar 1-5)
 2    3    4    5    6    7    8    ← BUFFER WEEK (Mar 1-5 close in progress)
 9   10   11   12   13   14   15    ← WEEK 4: PHASE 2 (Mar 9-15)
16   17   18   19   20   21   22    ← WEEK 5: PHASE 2 (Mar 16-22)
23   24   25   26   27   28   29    ← WEEK 6: PHASE 3 START (late March)
30   31                            

APRIL 2026
SUN  MON  TUE  WED  THU  FRI  SAT
           1    2    3    4    5    ← BLACKOUT BEGINS (Apr 1-5)
 6    7    8    9   10   11   12    ← BUFFER WEEK (Apr 1-5 close in progress)
13   14   15   16   17   18   19    ← WEEK 7: PHASE 3 (Apr 13-19)
20   21   22   23   24   25   26    ← WEEK 8: PHASE 4 FINAL (Apr 20-26)
```

---

## PHASE 1: PYTHON FOUNDATIONS (WEEKS 1–2)
**Goal:** Translate VBA knowledge to Python syntax  
**Total Hours:** 6 hours (3 hrs/week)  
**Deliverable:** Mini-project: Consolidate hardcoded GL list by cost center  
**Resources:** "Automate the Boring Stuff" (Free), Real Python (Free), DataCamp (Optional)

---

### **WEEK 1: February 3–9, 2026** ✅ ACTIVE LEARNING
**Study Window:** Wednesday Feb 5, 2–5 PM (3 hours)  
**Focus:** Data types, variables, loops, conditionals  
**Key Concept:** "Python is just VBA with different syntax"

#### **PRE-WEEK SETUP (Do by Feb 2):**
- [ ] Install Python 3.10+ from python.org
- [ ] Install VS Code or PyCharm Community Edition
- [ ] Create project folder: `C:\Users\Ahmed\month_end_automation\`
- [ ] Run Python: `python -c "import sys; print(sys.version)"` (confirm installation)
- [ ] Save test GL data file: `test_gl_data.csv` (sample with 20 GL transactions)

#### **STUDY PLAN (3 hours Wednesday)**

**Segment 1: Variables & Data Types (1.5 hours)**
- *Reading:* "Automate the Boring Stuff" Ch. 1 (online: automatetheboringstuff.com) – 30 min
  - Skip intro; focus on: integers, strings, floats, variable naming conventions
  - **VBA Parallel:** "Think of `x = 5` like `Dim x As Integer; x = 5`"
- *Video:* Real Python "Variables & Print Statements" (youtube or realpython.com) – 20 min
  - Watch at 1.5x speed; take 2–3 notes on surprising Python behavior
- *Code-Along Exercise:* 45 min
  - Write 5 small scripts in VS Code:
    1. `print("Hello, GL World")`
    2. Assign GL account code: `account = "1010-CC001"` and print it
    3. Calculate GL amount: `amount = 10000; print(f"Amount: ${amount:,.2f}")`
    4. Extract parts of account code using string methods (`.split()`)
    5. Create variables for GL transaction: account, amount, variance_pct
  - **Success:** All 5 scripts run without syntax errors

**Segment 2: Loops & Conditionals (1.5 hours)**
- *Video:* Real Python "For Loops in Python" – 20 min
  - Focus on: `for account in gl_list:` vs. VBA `For i = 1 To lastRow`
  - Watch the "Loop Through a Range" section
- *Reading:* Real Python "If Statements" or "Automate..." Ch. 2 – 20 min
  - Learn: `if variance > 0.05:` vs. VBA `If variance > 0.05 Then`
- *Code-Along Exercise:* 50 min
  - **Mini-Exercise 1:** Loop through 10 GL account codes; print each (15 min)
    ```python
    gl_accounts = ["1010-CC001", "1020-CC002", "1030-CC003", ...]
    for account in gl_accounts:
        print(account)
    ```
  - **Mini-Exercise 2:** Loop + conditional – flag high variances (25 min)
    ```python
    gl_list = [
        {"account": "1010-CC001", "variance": 0.032},
        {"account": "1020-CC002", "variance": 0.067},
        ...
    ]
    for item in gl_list:
        if item["variance"] > 0.05:
            print(f"ALERT: {item['account']} variance > 5%")
    ```
  - **Mini-Exercise 3:** Filter by cost center (10 min)
    - Adapt Exercise 2 to filter where account contains "CC001"

#### **WEEK 1 CHECKPOINT (Thursday Feb 6)**
- [ ] Run all 5 variable scripts—confirm no syntax errors
- [ ] Run loop-and-filter script—confirm correct output
- [ ] Note any confusing parts (share with coach in Week 2 checkpoint)
- [ ] **Confidence Pulse:** Rate 1–10 how natural Python feels vs. VBA (should be 5–6)

#### **RESOURCES USED:**
| Resource | Time | URL |
|---|---|---|
| "Automate the Boring Stuff" Ch. 1–2 | 1 hr | https://automatetheboringstuff.com/2e/chapter1/ |
| Real Python: Variables | 20 min | https://realpython.com/python-variables/ |
| Real Python: For Loops | 20 min | https://realpython.com/loops-in-python/ |
| Real Python: If Statements | 20 min | https://realpython.com/python-conditional-statements/ |

---

### **WEEK 2: February 10–16, 2026** ✅ ACTIVE LEARNING + PHASE 1 CAPSTONE
**Study Window:** Wednesday Feb 12, 2–5 PM (3 hours)  
**Focus:** String manipulation, functions, Phase 1 capstone project  
**Key Concept:** Functions are reusable logic blocks (like Excel formulas or VBA functions)

#### **STUDY PLAN (3 hours Wednesday)**

**Segment 1: String Manipulation & Functions (1.5 hours)**
- *Reading:* Real Python "String Methods" or "Automate..." Ch. 5 – 30 min
  - Focus on: `.upper()`, `.split()`, `.strip()`, f-strings
  - **VBA Parallel:** "f-strings are like CONCATENATE() or & operator"
- *Reading:* Real Python "Defining Functions" – 20 min
  - Focus on: parameters, return values, docstrings
  - **VBA Parallel:** "Functions work exactly like `Function myFunc(param) As Variant`"
- *Code-Along Exercise:* 40 min
  - **Mini-Exercise 1:** Parse GL account code (15 min)
    ```python
    def extract_cost_center(account_code):
        """Extract cost center from account code like '1010-CC001'"""
        parts = account_code.split("-")
        return parts[1]  # Return "CC001"
    
    # Test it:
    cc = extract_cost_center("1010-CC001")
    print(cc)
    ```
  - **Mini-Exercise 2:** Write a variance calculator function (15 min)
    ```python
    def calc_variance_pct(current, prior):
        """Calculate variance as percentage: (Current - Prior) / Prior"""
        return (current - prior) / prior
    
    # Test it:
    var = calc_variance_pct(10500, 10000)
    print(f"Variance: {var:.1%}")  # Output: Variance: 5.0%
    ```
  - **Mini-Exercise 3:** Combine functions (10 min)
    - Write a third function that takes a GL record and calls both above functions

**Segment 2: Phase 1 Capstone Mini-Project (1.5 hours)**
- *Deliverable:* "GL Consolidation Script" (consolidate by cost center)
- *Task:* Write a script that:
  1. Defines a hardcoded list of 20 GL transactions:
     ```python
     gl_data = [
         {"account": "1010-CC001", "amount": 5000, "variance_pct": 0.023},
         {"account": "1020-CC001", "amount": 3200, "variance_pct": 0.067},
         {"account": "1030-CC002", "amount": 8900, "variance_pct": -0.015},
         # ... 17 more records
     ]
     ```
  2. Loops through and groups by cost center (CC001, CC002, etc.)
  3. Sums amounts by cost center
  4. Flags any accounts where variance > 5% 
  5. Prints a summary report:
     ```
     ===== GL CONSOLIDATION SUMMARY =====
     Cost Center: CC001
       Total Amount: $8,200
       Transactions: 2
       High Variance Items: 1010-CC001 (6.7%)
     
     Cost Center: CC002
       Total Amount: $8,900
       Transactions: 1
       High Variance Items: None
     ```

- *Scaffolding Provided:* 
  - Use the functions you wrote in Segment 1
  - Outline provided (if stuck, ask coach)
  - Focus on logic, not perfection

- *Time Breakdown:*
  - Set up data structure (10 min)
  - Write loop & grouping logic (25 min)
  - Debug & refine (20 min)
  - Test with 2–3 GL records manually (5 min)

#### **WEEK 2 CHECKPOINT (Friday Feb 14)**
- [ ] Run capstone script—confirm outputs summary report correctly
- [ ] Verify calculations are accurate (spot-check 3–4 totals by hand)
- [ ] Share script with learning coach (code review)
- [ ] **Confidence Pulse:** Rate 1–10 how confident you feel writing Python (should be 6–7)
- [ ] **Readiness Confirmation:** "I understand variables, loops, conditionals, and functions"

#### **RESOURCES USED:**
| Resource | Time | URL |
|---|---|---|
| Real Python: String Methods | 30 min | https://realpython.com/python-strings/ |
| Real Python: Defining Functions | 20 min | https://realpython.com/defining-your-own-python-function/ |
| "Automate the Boring Stuff" Ch. 5 | 10 min | https://automatetheboringstuff.com/2e/chapter5/ |

#### **DELIVERABLE CHECKLIST:**
- ✅ 5 variable scripts from Week 1
- ✅ 2 reusable functions (extract_cost_center, calc_variance_pct)
- ✅ Phase 1 Capstone: GL consolidation script (consolidate by CC, flag >5% variance)
- ✅ Script runs end-to-end without errors
- ✅ Output matches expected consolidation summary

---

## BUFFER WEEK 1: February 17–23, 2026 ⏸️ NO FORMAL LEARNING
**Reason:** Month-end close for February (Feb 1–5) just completed; Ahmed is likely in catch-up mode  
**Recommended Activity:**
- Review Week 1–2 code; refactor if time permits
- Prepare GL sample data for Phase 2 (get Feb GL export from SAP if possible)
- Schedule Phase 2 kickoff call with coach
- **Rest—no new learning expected this week**

---

## PHASE 2: PANDAS ESSENTIALS (WEEKS 3–4)
**Goal:** Master DataFrames; automate GL reading, filtering, grouping, and exporting  
**Total Hours:** 6 hours (3 hrs/week, split across 2 weeks + buffer)  
**Deliverable:** Mini-project: Load & consolidate 10K-row SAP GL export to Excel  
**Resources:** DataCamp (Pandas Fundamentals), Real Python (Pandas articles), "Automate..." Ch. 12–13

---

### **WEEK 3: February 24–March 2, 2026** ⚠️ PARTIAL ACTIVE LEARNING (Mixed with Month-End Close)
**Study Window:** Monday Feb 24, 2–5 PM (3 hours) – *Note: Study BEFORE month-end starts*  
**Focus:** DataFrame fundamentals, reading data  
**Key Concept:** "DataFrames are like Excel tables; pandas is like Pivot Tables in code"

#### **SPECIAL NOTE: MARCH 1–5 BLACKOUT UPCOMING**
- **Study on Feb 24–25 ONLY** (before month-end chaos begins Mar 1)
- **NO LEARNING MAR 1–5** (Month-end close in progress)
- **Resume Mar 9** (after month-end complete)

#### **STUDY PLAN (3 hours Monday Feb 24)**

**Segment 1: DataFrame Basics & Reading Data (1.5 hours)**
- *Reading:* Real Python "Pandas DataFrame Basics" – 30 min
  - Focus on: creating DataFrames, `.head()`, `.info()`, `.shape`, `.describe()`
  - **Excel Parallel:** "Think of a DataFrame like an Excel table with rows and columns"
- *Interactive:* DataCamp "Pandas Fundamentals – Introduction to DataFrames" (if subscribed) – 25 min
  - OR watch YouTube: "Corey Schafer – Pandas Tutorial Pt. 1" (20 min)
  - Hands-on: Create a simple DataFrame, explore its structure
- *Code-Along Exercise:* 25 min
  - **Exercise 1:** Create a DataFrame from a hardcoded list (10 min)
    ```python
    import pandas as pd
    gl_data = [
        {"account": "1010-CC001", "amount": 5000},
        {"account": "1020-CC001", "amount": 3200},
        ...
    ]
    df = pd.DataFrame(gl_data)
    print(df)
    print(df.info())
    print(df.describe())
    ```
  - **Exercise 2:** Read actual GL CSV from SAP (15 min)
    - `df = pd.read_csv("C:\\Users\\Ahmed\\month_end_automation\\GL_Feb2026.csv")`
    - Explore: `print(df.head(10))`, `print(df.shape)`, `print(df.dtypes)`
    - **Goal:** Confirm GL loads correctly; no import errors

**Segment 2: Filtering & Exploring Real Data (1.5 hours)**
- *Reading:* Real Python "Selecting & Indexing Data" – 25 min
  - Focus on: `.loc[]`, `.iloc[]`, boolean indexing (filtering)
  - **Excel Parallel:** "Boolean indexing is like Excel's FILTER() or AutoFilter"
- *Code-Along Exercise:* 45 min
  - **Exercise 1:** Filter GL by cost center (20 min)
    ```python
    # Show only CC001 transactions
    cc001 = df[df["cost_center"] == "CC001"]
    print(cc001)
    ```
  - **Exercise 2:** Filter by amount threshold (15 min)
    ```python
    # Show only amounts > $5,000
    high_amounts = df[df["amount"] > 5000]
    print(high_amounts)
    ```
  - **Exercise 3:** Combine filters (10 min)
    ```python
    # Show CC001 transactions > $5,000
    filtered = df[(df["cost_center"] == "CC001") & (df["amount"] > 5000)]
    print(filtered)
    ```

#### **WEEK 3 CHECKPOINT (Monday Feb 24, before leaving for month-end)**
- [ ] Create DataFrame from hardcoded list—verify structure is correct
- [ ] Load actual Feb GL CSV—confirm 10K+ rows load without error
- [ ] Run 3 filter exercises—confirm boolean indexing works
- [ ] **Confidence Pulse:** "I understand DataFrames and basic filtering"

#### **BUFFER: MARCH 1–5 (BLACKOUT - MONTH-END CLOSE IN PROGRESS)**
- ⏸️ **NO LEARNING** – Ahmed is in month-end close crunch
- Save this: "Week 3 Checkpoint: DataFrame Basics Complete"

#### **RESOURCES USED:**
| Resource | Time | URL |
|---|---|---|
| Real Python: DataFrame Basics | 30 min | https://realpython.com/learning-paths/pandas-data-science/ |
| DataCamp: Intro to DataFrames (or YouTube) | 25 min | DataCamp (free tier) OR https://www.youtube.com/watch?v=vmEHCJofslg |
| Real Python: Selecting Data | 25 min | https://realpython.com/pandas-indexing-slicing/ |

---

### **WEEK 4: March 9–15, 2026** ✅ ACTIVE LEARNING (PHASE 2 CONTINUATION)
**Study Window:** Wednesday Mar 11, 2–5 PM (3 hours)  
**Focus:** Grouping, aggregation, merging (the heart of month-end automation)  
**Key Concept:** "Pandas groupby is like Excel Pivot Table; merge is like VLOOKUP"

#### **STUDY PLAN (3 hours Wednesday)**

**Segment 1: Grouping & Aggregation (1.5 hours)**
- *Reading:* Real Python "GroupBy Operations" – 30 min
  - Focus on: `.groupby()`, `.sum()`, `.count()`, `.mean()`, `.agg()`
  - **Excel Parallel:** "GroupBy is exactly like creating an Excel Pivot Table"
- *Interactive:* DataCamp "GroupBy Operations" or YouTube tutorial – 20 min
  - Watch example: group sales by region, sum by region
  - Apply to GL: group by cost center, sum amounts
- *Code-Along Exercise:* 40 min
  - **Exercise 1:** Group GL by cost center; sum amounts (15 min)
    ```python
    grouped = df.groupby("cost_center")["amount"].sum()
    print(grouped)
    # Output:
    # cost_center
    # CC001    8,200
    # CC002    8,900
    # ...
    ```
  - **Exercise 2:** Multi-level grouping (15 min)
    ```python
    # Group by cost center AND account code
    grouped = df.groupby(["cost_center", "account_code"])["amount"].sum()
    print(grouped)
    ```
  - **Exercise 3:** Add multiple aggregations (10 min)
    ```python
    # Sum amount, count transactions, calculate average
    summary = df.groupby("cost_center").agg({
        "amount": ["sum", "count", "mean"]
    })
    print(summary)
    ```

**Segment 2: Merging Data & Joining Tables (1.5 hours)**
- *Reading:* Real Python "Merging/Joining DataFrames" – 25 min
  - Focus on: `.merge()`, `.join()`, left/inner joins
  - **Excel Parallel:** "Merge is like VLOOKUP to join GL with Chart of Accounts"
- *Code-Along Exercise:* 55 min
  - **Exercise 1:** Create a Chart of Accounts lookup table (15 min)
    ```python
    coa = pd.DataFrame({
        "account_code": ["1010", "1020", "1030"],
        "account_name": ["Cash", "Receivables", "Inventory"]
    })
    print(coa)
    ```
  - **Exercise 2:** Merge GL with CoA to add account names (20 min)
    ```python
    # Merge to enrich GL with account names
    enriched = df.merge(coa, on="account_code", how="left")
    print(enriched[["account_code", "account_name", "amount"]])
    ```
  - **Exercise 3:** Group enriched data (20 min)
    ```python
    # Group enriched GL by cost center and account name
    summary = enriched.groupby(["cost_center", "account_name"])["amount"].sum()
    print(summary)
    ```

#### **WEEK 4 CHECKPOINT (Friday Mar 13)**
- [ ] Run groupby exercises—verify correct totals by cost center
- [ ] Merge GL with CoA—confirm account names appear correctly
- [ ] Multi-level grouping—verify output format matches expected
- [ ] Share code with coach; request feedback
- [ ] **Confidence Pulse:** "I can group and merge GL data like a Pivot Table"

#### **RESOURCES USED:**
| Resource | Time | URL |
|---|---|---|
| Real Python: GroupBy Operations | 30 min | https://realpython.com/pandas-groupby/ |
| DataCamp: GroupBy (or YouTube) | 20 min | DataCamp (free tier) OR https://www.youtube.com/watch?v=txMdrllweUI |
| Real Python: Merging DataFrames | 25 min | https://realpython.com/pandas-merge-join-append/ |

#### **PHASE 2 CAPSTONE PREP:**
- By end of Week 4, have ready:
  - ✅ GL CSV file (10K+ rows from SAP)
  - ✅ Chart of Accounts CSV (lookup table)
  - ✅ Understanding of final consolidation structure (how to group, aggregate, export)

---

### **WEEK 4.5: March 16–22, 2026** ⚠️ EXTENDED PHASE 2 (Continued from Week 4)
**Study Window:** Wednesday Mar 18, 2–5 PM (3 hours)  
**Focus:** Phase 2 Capstone + writing to Excel  
**Key Concept:** "Export consolidation to Excel, ready for MBR"

#### **STUDY PLAN (3 hours Wednesday)**

**Segment 1: Writing Data to Excel (1 hour)**
- *Reading:* Real Python "Writing DataFrames to Excel" or pandas docs – 20 min
  - Focus on: `to_excel()`, ExcelWriter for multiple sheets, basic formatting
- *Code-Along Exercise:* 40 min
  - **Exercise 1:** Write DataFrame to Excel (20 min)
    ```python
    # Write consolidated summary to Excel
    summary.to_excel("GL_Consolidation_Feb2026.xlsx", sheet_name="Summary")
    print("✓ File written to GL_Consolidation_Feb2026.xlsx")
    ```
  - **Exercise 2:** Write multiple sheets (20 min)
    ```python
    # Use ExcelWriter to write summary + detail sheets
    with pd.ExcelWriter("GL_Report_Feb2026.xlsx") as writer:
        summary.to_excel(writer, sheet_name="Summary")
        enriched.to_excel(writer, sheet_name="Detail")
    print("✓ Multi-sheet file created")
    ```

**Segment 2: Phase 2 Capstone Mini-Project (2 hours)**
- *Deliverable:* "GL Consolidation to Excel" (real SAP data)
- *Task:* Write a script that:
  1. Reads GL CSV (10K+ rows)
  2. Reads Chart of Accounts lookup
  3. Merges GL with CoA (enrich with account names)
  4. Consolidates:
     - Sum by cost center + account
     - Count transactions per cost center
  5. Exports to Excel:
     - Sheet 1: "Summary" (consolidated totals by CC + Account)
     - Sheet 2: "Detail" (all GL transactions, enriched)
  6. Prints report to console:
     ```
     ===== GL CONSOLIDATION REPORT (FEB 2026) =====
     Total GL Records: 10,847
     Records after merge: 10,847
     Unique Cost Centers: 12
     Summary exported to: GL_Consolidation_Feb2026.xlsx
     ```

- *Time Breakdown:*
  - Load GL and CoA CSVs (10 min)
  - Merge & enrich (15 min)
  - Consolidate by CC + Account (20 min)
  - Write multi-sheet Excel (10 min)
  - Test and validate (5 min)

#### **WEEK 4.5 CHECKPOINT (Friday Mar 20)**
- [ ] Script reads 10K+ GL rows without error
- [ ] Merge with CoA successful (no null values)
- [ ] Consolidation totals are reasonable (spot-check against prior period)
- [ ] Excel file created with 2 sheets: Summary + Detail
- [ ] Script runs in <2 minutes
- [ ] **Confidence Pulse:** "I can automate GL loading and consolidation"

#### **RESOURCES USED:**
| Resource | Time | URL |
|---|---|---|
| Real Python: Writing to Excel | 20 min | https://realpython.com/openpyxl-excel-spreadsheets-python/ |
| Pandas Docs: ExcelWriter | 10 min | https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html |

#### **DELIVERABLE CHECKLIST (END OF PHASE 2):**
- ✅ Phase 2 Capstone: GL consolidation script (read CSV, merge, group, export Excel)
- ✅ Script outputs 2-sheet Excel file (Summary + Detail)
- ✅ Consolidation totals validated against expected (or prior period)
- ✅ Script runs cleanly; no errors

---

## BUFFER WEEK 2: March 23–29, 2026 ⏸️ OPTIONAL CATCH-UP / REST
**Reason:** Phase 2 might run long; buffer week allows for catch-up without pressure  
**Recommended Activity:**
- If on track: rest, review Phase 2 notes
- If behind: spend 2–3 hours reviewing groupby and merge concepts
- Prepare GL + CoA data for Phase 3 (real March GL export from SAP)
- **PHASE 3 KICKOFF:** Friday Mar 27 (brief coach call to confirm readiness)

---

## PHASE 3: FINANCIAL AUTOMATION (WEEKS 5–7)
**Goal:** Build production-ready month-end close automation with validation, variance, and error handling  
**Total Hours:** 10 hours (3+ hrs/week across 3 weeks)  
**Deliverable:** Major project: End-to-end month-end close script (working prototype)  
**Resources:** Real Python (error handling, openpyxl), DataCamp (advanced), 1-on-1 coach (optional)

---

### **WEEK 5: March 30–April 5, 2026** ⚠️ PARTIAL ACTIVE LEARNING (Month-End Close Overlap)
**Study Window:** Monday Mar 30, 2–5 PM (3 hours) – *Study BEFORE April month-end starts*  
**Focus:** Data validation, consolidation logic, error handling intro  
**Key Concept:** "Validation catches bad data before consolidation"

#### **SPECIAL NOTE: APRIL 1–5 BLACKOUT UPCOMING**
- **Study on Mar 30–31 ONLY** (before month-end chaos begins Apr 1)
- **NO LEARNING APR 1–5** (Month-end close in progress)
- **Resume Apr 13** (after month-end complete)

#### **STUDY PLAN (3 hours Monday Mar 30)**

**Segment 1: Data Validation & Cleaning (1.5 hours)**
- *Reading:* Real Python "Data Cleaning with Pandas" or DataCamp – 30 min
  - Focus on: checking for null values, duplicates, data type mismatches
  - **Finance Context:** "Missing cost center? Duplicate account entry? Catch it before consolidation"
- *Code-Along Exercise:* 60 min
  - **Exercise 1:** Check for null values (15 min)
    ```python
    # Check for missing values
    print(df.isnull().sum())  # Count nulls per column
    
    # Flag records with null cost_center
    missing_cc = df[df["cost_center"].isnull()]
    print(f"Records missing cost center: {len(missing_cc)}")
    ```
  - **Exercise 2:** Validate account codes (20 min)
    ```python
    # Validate against known accounts (Chart of Accounts)
    valid_accounts = coa["account_code"].unique()
    invalid = df[~df["account_code"].isin(valid_accounts)]
    print(f"Unknown accounts: {len(invalid)}")
    print(invalid[["account_code", "amount"]])
    ```
  - **Exercise 3:** Check for duplicates (15 min)
    ```python
    # Find duplicate GL entries
    duplicates = df[df.duplicated(subset=["account_code", "cost_center", "amount"], keep=False)]
    print(f"Duplicate records: {len(duplicates)}")
    ```
  - **Exercise 4:** Amount reasonableness check (10 min)
    ```python
    # Flag amounts outside expected range (e.g., > $1M is suspicious)
    suspicious = df[df["amount"] > 1000000]
    print(f"Suspicious amounts: {len(suspicious)}")
    ```

**Segment 2: Error Handling Intro (1.5 hours)**
- *Reading:* Real Python "Python Try Except" – 25 min
  - Focus on: try/except blocks, exception types
  - **VBA Parallel:** "Like `On Error Resume Next` but more controlled"
- *Code-Along Exercise:* 55 min
  - **Exercise 1:** Basic try/except (15 min)
    ```python
    try:
        df = pd.read_csv("GL_March2026.csv")
        print("✓ GL file loaded successfully")
    except FileNotFoundError:
        print("✗ Error: GL file not found. Check file path.")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
    ```
  - **Exercise 2:** Wrap consolidation in try/except (20 min)
    ```python
    try:
        # Load data
        df = pd.read_csv("GL_March2026.csv")
        # Validate
        assert len(df) > 0, "GL file is empty"
        assert df["cost_center"].isnull().sum() == 0, "Missing cost centers"
        # Consolidate
        summary = df.groupby("cost_center")["amount"].sum()
        print("✓ Consolidation successful")
    except AssertionError as e:
        print(f"✗ Validation failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
    ```
  - **Exercise 3:** Add logging (20 min)
    ```python
    import logging
    logging.basicConfig(filename="month_end_log.txt", level=logging.INFO)
    
    try:
        df = pd.read_csv("GL_March2026.csv")
        logging.info(f"GL loaded: {len(df)} rows")
        # ... consolidation logic ...
        logging.info("Consolidation complete")
    except Exception as e:
        logging.error(f"Error: {e}")
    ```

#### **WEEK 5 CHECKPOINT (Monday Mar 30, before leaving for month-end)**
- [ ] Run validation exercises—confirm nulls, duplicates, invalid accounts detected
- [ ] Wrap consolidation in try/except—test error handling
- [ ] Create log file—verify logging works
- [ ] **Confidence Pulse:** "I can catch data quality issues before consolidation"

#### **BUFFER: APRIL 1–5 (BLACKOUT - MONTH-END CLOSE IN PROGRESS)**
- ⏸️ **NO LEARNING** – Ahmed is in month-end close crunch

#### **RESOURCES USED:**
| Resource | Time | URL |
|---|---|---|
| Real Python: Data Cleaning | 30 min | https://realpython.com/python-pandas-data-cleaning/ |
| Real Python: Try Except | 25 min | https://realpython.com/python-exceptions/ |
| Pandas Docs: isnull, duplicated | 10 min | https://pandas.pydata.org/docs/ |

---

### **WEEK 6: April 13–19, 2026** ✅ ACTIVE LEARNING (PHASE 3 CONTINUATION)
**Study Window:** Wednesday Apr 15, 2–5 PM (3 hours)  
**Focus:** Variance calculation, multi-level consolidation, output formatting  
**Key Concept:** "Variance is the core insight for the MBR"

#### **STUDY PLAN (3 hours Wednesday)**

**Segment 1: Variance Calculation & Flagging (1.5 hours)**
- *Setup:* Have prior month GL (March 2026) loaded separately as reference
- *Code-Along Exercise:* 90 min
  - **Exercise 1:** Calculate variance vs. prior month (25 min)
    ```python
    # Load current month and prior month GL
    current = pd.read_csv("GL_April2026.csv")
    prior = pd.read_csv("GL_March2026.csv")
    
    # Consolidate both
    current_summary = current.groupby("cost_center")["amount"].sum()
    prior_summary = prior.groupby("cost_center")["amount"].sum()
    
    # Calculate variance
    variance = current_summary - prior_summary
    variance_pct = (variance / prior_summary.abs()) * 100
    
    print("Variance vs Prior Month:")
    print(variance)
    print("\nVariance %:")
    print(variance_pct)
    ```
  - **Exercise 2:** Flag high variances (20 min)
    ```python
    # Flag variances > 5%
    high_variance = variance_pct[variance_pct.abs() > 5]
    print("Cost Centers with Variance > 5%:")
    print(high_variance)
    ```
  - **Exercise 3:** Create variance detail table (25 min)
    ```python
    # Merge variance info into summary
    summary_with_variance = pd.DataFrame({
        "Prior_Month": prior_summary,
        "Current_Month": current_summary,
        "Variance_Amount": variance,
        "Variance_%": variance_pct,
        "Flag": ["HIGH" if abs(v) > 5 else "OK" for v in variance_pct]
    })
    print(summary_with_variance)
    ```
  - **Exercise 4:** Export variance report to Excel (20 min)
    ```python
    summary_with_variance.to_excel("Variance_Report_Apr2026.xlsx")
    print("✓ Variance report exported")
    ```

**Segment 2: Multi-Level Consolidation & Output Formatting (1.5 hours)**
- *Context:* Real month-end consolidation structure (CC + Account, with eliminations if applicable)
- *Code-Along Exercise:* 90 min
  - **Exercise 1:** Multi-level grouping (25 min)
    ```python
    # Consolidate by cost center AND account code (multi-level)
    multi_summary = df.groupby(["cost_center", "account_code"]).agg({
        "amount": ["sum", "count"],
        "account_name": "first"
    })
    print(multi_summary)
    ```
  - **Exercise 2:** Add intercompany elimination (if applicable) (20 min)
    ```python
    # Example: eliminate intercompany transactions
    # (transactions between internal entities should net to zero)
    df_no_ic = df[~df["account_code"].isin(["9100", "9101"])]  # IC accounts
    summary_no_ic = df_no_ic.groupby("cost_center")["amount"].sum()
    print(summary_no_ic)
    ```
  - **Exercise 3:** Format Excel output (25 min)
    ```python
    # Export with formatting
    with pd.ExcelWriter("GL_Summary_Apr2026.xlsx", engine="openpyxl") as writer:
        summary_with_variance.to_excel(writer, sheet_name="Summary")
    
    # Load the workbook and format (if time permits)
    # - Add bold headers
    # - Format currency ($ with 2 decimals)
    # - Add totals row
    ```
  - **Exercise 4:** Create professional summary report (20 min)
    ```python
    # Print summary stats for the report
    print("=" * 50)
    print("GL CONSOLIDATION SUMMARY - APRIL 2026")
    print("=" * 50)
    print(f"Total GL Records: {len(df):,}")
    print(f"Total Amount: ${df['amount'].sum():,.2f}")
    print(f"Unique Cost Centers: {df['cost_center'].nunique()}")
    print(f"High Variance Items (>5%): {len(high_variance)}")
    print("=" * 50)
    ```

#### **WEEK 6 CHECKPOINT (Friday Apr 17)**
- [ ] Calculate variance vs. prior month (March)—verify calculations are correct
- [ ] Flag high variances (>5%)—confirm list is reasonable
- [ ] Export variance report to Excel—format looks professional
- [ ] Multi-level consolidation works—CC + Account grouping correct
- [ ] Summary stats printed correctly
- [ ] **Confidence Pulse:** "I can calculate and report GL variance for the MBR"

#### **RESOURCES USED:**
| Resource | Time | URL |
|---|---|---|
| Real Python: Aggregation Functions | 20 min | https://realpython.com/pandas-groupby/ |
| Pandas Docs: agg() | 10 min | https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html |
| Openpyxl Docs: Formatting | 15 min | https://openpyxl.readthedocs.io/ |

---

### **WEEK 7: April 20–26, 2026** ✅ ACTIVE LEARNING (PHASE 3 CAPSTONE)
**Study Window:** Wednesday Apr 22, 2–5 PM (3.5 hours) – *Extra 0.5 hrs for capstone*  
**Focus:** Phase 3 Capstone: End-to-end month-end close script  
**Key Concept:** "Integrate validation, consolidation, variance, and error handling into one working script"

#### **STUDY PLAN (3.5 hours Wednesday)**

**Segment 1: Code Integration & Testing (3.5 hours)**
- *Deliverable:* "Month-End Close Automation Script v1.0" (working prototype)
- *Task:* Integrate all Phase 3 concepts into one production-ready script:

```python
"""
Month-End Close Automation Script v1.0
Purpose: Automate GL consolidation, variance analysis, and MBR reporting
Author: Ahmed Ali
Date: April 2026
"""

import pandas as pd
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename="month_end_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data(gl_file, coa_file):
    """Load GL and Chart of Accounts from CSV files"""
    try:
        gl = pd.read_csv(gl_file)
        coa = pd.read_csv(coa_file)
        logging.info(f"GL loaded: {len(gl)} rows")
        logging.info(f"CoA loaded: {len(coa)} rows")
        return gl, coa
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise

def validate_data(gl, coa):
    """Validate GL data quality"""
    errors = []
    
    # Check for null cost centers
    if gl["cost_center"].isnull().any():
        count = gl["cost_center"].isnull().sum()
        errors.append(f"Missing cost centers: {count} records")
        logging.warning(f"Missing cost centers: {count}")
    
    # Check for unknown accounts
    valid_accounts = coa["account_code"].unique()
    unknown = gl[~gl["account_code"].isin(valid_accounts)]
    if len(unknown) > 0:
        errors.append(f"Unknown accounts: {len(unknown)} records")
        logging.warning(f"Unknown accounts: {len(unknown)}")
    
    # Check for duplicates
    if gl.duplicated(subset=["account_code", "cost_center"]).any():
        count = gl.duplicated(subset=["account_code", "cost_center"]).sum()
        errors.append(f"Potential duplicates: {count} records")
        logging.warning(f"Duplicates detected: {count}")
    
    if errors:
        logging.warning(f"Validation issues: {'; '.join(errors)}")
        return False
    
    logging.info("✓ Data validation passed")
    return True

def consolidate_gl(gl, coa):
    """Consolidate GL by cost center and account; enrich with account names"""
    # Merge with CoA
    enriched = gl.merge(coa, on="account_code", how="left")
    
    # Consolidate
    summary = enriched.groupby(["cost_center", "account_code"]).agg({
        "amount": "sum",
        "account_name": "first"
    }).reset_index()
    
    summary.columns = ["cost_center", "account_code", "total_amount", "account_name"]
    
    logging.info(f"Consolidation complete: {len(summary)} cost center + account combinations")
    return summary

def calculate_variance(current_summary, prior_summary):
    """Calculate variance vs. prior month"""
    # Merge current and prior
    variance_df = current_summary.merge(
        prior_summary,
        on=["cost_center", "account_code"],
        how="left",
        suffixes=("_current", "_prior")
    )
    
    # Calculate variance
    variance_df["variance_amount"] = variance_df["total_amount_current"] - variance_df["total_amount_prior"].fillna(0)
    variance_df["variance_pct"] = (variance_df["variance_amount"] / variance_df["total_amount_prior"].abs()) * 100
    variance_df["flag"] = ["HIGH" if abs(v) > 5 else "OK" for v in variance_df["variance_pct"]]
    
    logging.info(f"Variance calculation complete: {len(variance_df[variance_df['flag'] == 'HIGH'])} high variance items")
    return variance_df

def export_to_excel(gl, summary, variance_df, output_file):
    """Export GL, summary, and variance to Excel"""
    try:
        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
            summary.to_excel(writer, sheet_name="Summary", index=False)
            variance_df.to_excel(writer, sheet_name="Variance", index=False)
            gl.to_excel(writer, sheet_name="Detail", index=False)
        
        logging.info(f"✓ Excel file created: {output_file}")
        return True
    except Exception as e:
        logging.error(f"Error writing Excel: {e}")
        return False

def main():
    """Main execution"""
    print("=" * 60)
    print("MONTH-END CLOSE AUTOMATION")
    print("=" * 60)
    
    try:
        # Load data
        gl, coa = load_data(
            "GL_April2026.csv",
            "Chart_of_Accounts.csv"
        )
        
        # Validate
        if not validate_data(gl, coa):
            print("⚠ Validation warnings (see log). Proceeding...")
        
        # Consolidate
        summary = consolidate_gl(gl, coa)
        
        # Load prior month for variance
        prior_gl, _ = load_data("GL_March2026.csv", "Chart_of_Accounts.csv")
        prior_summary = consolidate_gl(prior_gl, coa)
        
        # Calculate variance
        variance_df = calculate_variance(summary, prior_summary)
        
        # Export
        if export_to_excel(gl, summary, variance_df, "GL_Consolidation_Apr2026.xlsx"):
            print("\n✓ SUCCESS: Month-end close automation complete")
            print(f"  - GL Records: {len(gl):,}")
            print(f"  - Summary Rows: {len(summary):,}")
            print(f"  - High Variance Items: {len(variance_df[variance_df['flag'] == 'HIGH'])}")
            print(f"  - Output: GL_Consolidation_Apr2026.xlsx")
        else:
            print("\n✗ FAILED: Error exporting to Excel (see log)")
        
        logging.info("=" * 60)
        logging.info("MONTH-END CLOSE COMPLETE")
        logging.info("=" * 60)
    
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        logging.error(f"Fatal error: {e}")

if __name__ == "__main__":
    main()
```

- *Time Breakdown (3.5 hours):*
  - Review script structure (15 min)
  - Write each function (load, validate, consolidate, variance, export) (90 min)
  - Integrate functions into main() (20 min)
  - Test end-to-end with real March/April GL (30 min)
  - Debug and refine (25 min)

#### **WEEK 7 CHECKPOINT (Friday Apr 24)**
- [ ] Script runs end-to-end without syntax errors
- [ ] All functions execute (load, validate, consolidate, variance, export)
- [ ] Excel output file created with 3 sheets: Summary, Variance, Detail
- [ ] Summary totals match prior manual consolidation (within $0)
- [ ] High variance items are correctly flagged
- [ ] Log file created with execution timestamps
- [ ] Script completes in <2 minutes
- [ ] Share script with coach; request code review
- [ ] **Confidence Pulse:** "I have a working automation script; I could hand it to someone else"

#### **DELIVERABLE CHECKLIST (END OF PHASE 3):**
- ✅ Month-End Close Automation Script v1.0 (complete)
- ✅ Script includes: load, validate, consolidate, variance, export
- ✅ Error handling with logging
- ✅ Excel output with 3 sheets (Summary, Variance, Detail)
- ✅ Validation of output vs. prior manual consolidation (match or <1% variance)
- ✅ Script is working prototype; ready for Phase 4 polish

---

## BUFFER WEEK 3: April 27–May 3, 2026 ⏸️ NO FORMAL LEARNING (Month-End Blackout)
**Reason:** May 1–5 month-end close (May numbers due)  
**Recommended Activity:**
- Review Phase 3 capstone script; ask coach for feedback
- Document any bugs or edge cases discovered during April month-end
- Prepare notes for Phase 4 (documentation, scheduling)
- **Rest—no new learning expected this week**

---

## PHASE 4: REFINEMENT & PRODUCTION READINESS (WEEK 8)
**Goal:** Polish code, add documentation, schedule for production use  
**Total Hours:** 2 hours (final week)  
**Deliverable:** Production-ready script + user guide + scheduled job  
**Resources:** PEP 257 (Docstrings), Real Python (Code Quality), Windows Task Scheduler / Cron

---

### **WEEK 8: May 4–10, 2026** ✅ FINAL POLISH & DEPLOYMENT
**Study Window:** Wednesday May 6, 2–3 PM (2 hours) – *Final short session*  
**Focus:** Documentation, cleanup, scheduling, handoff  
**Key Concept:** "A colleague should be able to run this script without my help"

#### **STUDY PLAN (2 hours Wednesday)**

**Segment 1: Code Documentation & Comments (0.5 hours)**
- *Task:* Add docstrings and comments to script
- *Deliverable:* Fully commented script
  - Every function has a docstring (what it does, inputs, outputs)
  - Complex logic (variance calc, eliminations) has inline comments
  - Variable names are clear and self-documenting
- *Example:*
  ```python
  def validate_data(gl, coa):
      """
      Validate GL data quality.
      
      Parameters:
          gl (DataFrame): General Ledger data
          coa (DataFrame): Chart of Accounts lookup
      
      Returns:
          bool: True if validation passes, False if warnings found
      
      Checks:
          - Missing cost centers
          - Unknown account codes (not in CoA)
          - Duplicate GL entries
      """
      # ... function body ...
  ```

**Segment 2: User Guide & Scheduling (1.5 hours)**
- *Deliverable 1:* 1-page User Guide (README.md)
  ```markdown
  # GL Consolidation Automation - User Guide
  
  ## What This Script Does
  - Loads GL export from SAP
  - Validates data quality
  - Consolidates GL by cost center + account
  - Calculates variance vs. prior month
  - Exports to Excel (Summary + Variance + Detail sheets)
  
  ## How to Use
  1. Export GL from SAP to `GL_<Month><Year>.csv`
  2. Run: `python month_end_automation.py`
  3. Output: `GL_Consolidation_<Month><Year>.xlsx`
  
  ## Troubleshooting
  - **Error: File not found** → Check file names and folder location
  - **Missing cost centers** → Verify GL export includes all required fields
  - **Check the log file** → `month_end_automation.log` has detailed messages
  ```

- *Deliverable 2:* Schedule script to run automatically
  - **Option A (Windows):** Task Scheduler
    - Create scheduled task: "Run month_end_automation.py on 1st of month at 6 AM"
    - Script runs unattended
  - **Option B (Mac/Linux):** Cron job
    - `0 6 1 * * /usr/bin/python3 /path/to/month_end_automation.py`
    - Scheduled to run 1st of each month at 6 AM
  - *Time Breakdown (30 min)*
    - Learn scheduling (10 min)
    - Set up scheduled job (15 min)
    - Test (confirm runs unattended) (5 min)

#### **WEEK 8 CHECKPOINT (Friday May 8)**
- [ ] Script is fully commented with docstrings
- [ ] User Guide (README.md) is complete and clear
- [ ] Scheduled job set up (Task Scheduler or cron)
- [ ] Test run confirms script executes unattended
- [ ] All debug/temp code removed
- [ ] Final code review with coach ✓ Approved
- [ ] **Final Confidence Pulse:** "I can hand this to anyone and they can use it"

#### **DELIVERABLE CHECKLIST (END OF PHASE 4 / FINAL):**
- ✅ Fully commented, production-ready script
- ✅ User Guide (1-page README)
- ✅ Scheduled job configured (automatic monthly execution)
- ✅ Log file tracking execution
- ✅ Excel output is professional and ready for MBR
- ✅ A non-technical colleague could follow the user guide and run the script

#### **RESOURCES USED:**
| Resource | Time | URL |
|---|---|---|
| PEP 257: Docstring Conventions | 15 min | https://www.python.org/dev/peps/pep-0257/ |
| Real Python: Writing Docstrings | 10 min | https://realpython.com/documenting-python-code/ |
| Windows Task Scheduler Tutorial (or Cron) | 15 min | https://docs.microsoft.com/en-us/windows/win32/taskschd/ |

---

## SUMMARY: 8-WEEK SCHEDULE AT A GLANCE

| **Week** | **Date** | **Phase** | **Focus** | **Study Hours** | **Status** |
|---|---|---|---|---|---|
| **1** | Feb 3–9 | Phase 1 | Variables, loops, conditionals | 3 hrs | ✅ Active |
| **2** | Feb 10–16 | Phase 1 | Functions, Phase 1 capstone | 3 hrs | ✅ Active |
| **BUFFER 1** | Feb 17–23 | — | Month-end prep, rest | 0 hrs | ⏸️ No learning |
| **3** | Feb 24–Mar 2 | Phase 2 | DataFrame basics, reading data | 3 hrs | ✅ Active (pre-blackout) |
| **BUFFER 2** | Mar 1–5 | — | **Month-end close (BLACKOUT)** | 0 hrs | ⏸️ No learning |
| **3.5** | Mar 9–15 | Phase 2 | Grouping, merging, consolidation | 3 hrs | ✅ Active |
| **4** | Mar 16–22 | Phase 2 | Phase 2 capstone, export to Excel | 3 hrs | ✅ Active |
| **BUFFER 3** | Mar 23–29 | — | Catch-up, rest, Phase 3 prep | 0–3 hrs | ⏸️ Optional |
| **5** | Mar 30–Apr 5 | Phase 3 | Validation, error handling | 3 hrs | ✅ Active (pre-blackout) |
| **BUFFER 4** | Apr 1–5 | — | **Month-end close (BLACKOUT)** | 0 hrs | ⏸️ No learning |
| **6** | Apr 13–19 | Phase 3 | Variance, multi-level consolidation | 3 hrs | ✅ Active |
| **7** | Apr 20–26 | Phase 3 | Phase 3 capstone, integration | 3.5 hrs | ✅ Active |
| **BUFFER 5** | Apr 27–May 3 | — | Month-end prep, rest | 0 hrs | ⏸️ No learning |
| **8** | May 4–10 | Phase 4 | Documentation, scheduling, handoff | 2 hrs | ✅ Final |
| **TOTAL** | **8 weeks** | **All 4 phases** | **Python + Pandas automation** | **24 hrs** | ✅ Complete |

---

## MONTHLY STUDY CALENDAR

### **FEBRUARY 2026**
```
Sun  Mon  Tue  Wed  Thu  Fri  Sat
                                 1
  2    3    4   [5]   6    7    8    ← Week 1 study: Wed Feb 5
  9   10   11  [12]  13   14   15    ← Week 2 study: Wed Feb 12
 16   17   18   19   20   21   22    ← Buffer (rest)
 23   24   25  [26]  27   28        ← Phase 2 prep: Wed Feb 24 (pre-blackout)
```

### **MARCH 2026**
```
Sun  Mon  Tue  Wed  Thu  Fri  Sat
                                 1    ← BLACKOUT STARTS (Mar 1–5)
  2    3    4    5    6    7    8    ← Buffer (month-end close)
  9   10   11  [12]  13   14   15    ← Phase 2 study: Wed Mar 12
 16   17   18  [19]  20   21   22    ← Phase 2 capstone: Wed Mar 19
 23   24   25   26   27  [28]  29    ← Optional buffer: Friday call
 30   31                            
```

### **APRIL 2026**
```
Sun  Mon  Tue  Wed  Thu  Fri  Sat
           1    2    3    4    5    ← BLACKOUT STARTS (Apr 1–5)
  6    7    8    9   10   11   12    ← Buffer (month-end close)
 13   14   15  [16]  17   18   19    ← Phase 3 study: Wed Apr 16
 20   21   22  [23]  24   25   26    ← Phase 3 capstone: Wed Apr 23
 27   28   29   30                  ← Buffer (prep for May month-end)
```

### **MAY 2026**
```
Sun  Mon  Tue  Wed  Thu  Fri  Sat
                                1    ← BLACKOUT STARTS (May 1–5)
  2    3    4    5    6   [7]   8    ← Phase 4 final: Wed May 7 (2 hrs)
  9   10   11   12   13   14   15
```

---

## WEEKLY ROUTINE (Standard Non-Blackout Week)

**Every Week (except blackout weeks):**
- **Monday:** Prepare resources; get 10 min summary of week's focus
- **Tuesday:** Read/watch resource materials (1–1.5 hrs, can break into 2–3 sessions)
- **Wednesday 2–5 PM:** Hands-on coding session (2–3 hrs)
- **Thursday:** Run code exercises again; verify correctness
- **Friday 1 PM:** Brief checkpoint call with coach (15–20 min)
  - Share code; get feedback
  - Clarify blockers
  - Confirm readiness for next week

---

## MONTHLY CHECKPOINT CALLS WITH COACH

| **Week** | **Date** | **Duration** | **Focus** |
|---|---|---|---|
| **Week 2** | Friday, Feb 14 | 15 min | Phase 1 mastery checkpoint: "Show me your functions and capstone script" |
| **Week 4.5** | Friday, Mar 20 | 20 min | Phase 2 capstone review: "Can you load and consolidate real GL?" |
| **Week 6** | Friday, Apr 17 | 20 min | Phase 3 progress: "Does your variance match expected? Any blockers?" |
| **Week 8** | Friday, May 8 | 20 min | Final review: "Is your script production-ready? Can someone else use it?" |

---

## RED FLAGS & ADJUSTMENTS

### **If Ahmed Falls Behind:**
- **Week 2 checkpoint:** "I don't feel confident with functions yet"
  - → Extend Phase 1 by 1 week; move Phase 2 start to Week 4
  - → Recommended: 10–12 week timeline instead of 8
- **Week 4.5 checkpoint:** "Pandas groupby still confuses me"
  - → Extend Phase 2; take extra week for practice
  - → Revisit Real Python articles on groupby/merge
- **Week 6 checkpoint:** "My consolidation output doesn't match expected"
  - → Pause Phase 3; spend extra week debugging Phase 2
  - → Compare script output to manual consolidation line-by-line

### **If Ahmed Accelerates:**
- **Week 3:** Can combine Phase 2 "DataFrame" + "Filtering" into one week
- **Week 5:** Can add SQL basics (querying GL directly from SAP) as stretch goal
- **Post-Week 8:** Can start Phase 4+ early (SQL, predictive modeling)

---

## RESOURCE COST SUMMARY

| **Resource** | **Cost** | **Weeks Used** | **Status** |
|---|---|---|---|
| "Automate the Boring Stuff" (free online) | $0 | 1–2, 3–4 | ✓ Included |
| Real Python (free articles) | $0 | All weeks | ✓ Included |
| DataCamp Fundamentals (monthly) | $40–50 | 3–4, 5–7 | Within budget |
| Windows Task Scheduler / Cron | $0 | Week 8 | ✓ Free (OS feature) |
| Openpyxl docs (free) | $0 | Weeks 3–4, 6–8 | ✓ Free |
| **TOTAL ESTIMATED COST** | **~$150–200** | **8 weeks** | ✓ **Within $1000 budget** |

---

## SUCCESS CRITERIA (END OF 8 WEEKS)

Ahmed will have achieved the learning goal if:

✅ **Automation Script:** Working Python script that automates 60–80% of month-end close  
✅ **Time Savings:** Runs in <2 minutes (vs. 2–3 hours manual)  
✅ **Accuracy:** Output matches manual consolidation dollar-for-dollar  
✅ **Usability:** Non-technical colleague can follow user guide and run script  
✅ **Production Ready:** Script has error handling, logging, scheduling, documentation  
✅ **Confidence:** Ahmed can read, write, and debug Python; feels comfortable with pandas  

---

## POST-8-WEEK ROADMAP (Future Learning)

**Months 3–4 (Optional stretch goals):**
- Learn SQL to query GL directly from SAP (eliminate CSV export step)
- Estimated effort: 4–6 hours over 4 weeks
- Impact: Reduce month-end automation from 2 min to 30 sec

**Months 5–8 (Future priority):**
- NumPy + scikit-learn for predictive variance modeling
- Build ML model to forecast month-end variance 2–3 weeks ahead
- Estimated effort: 12–16 hours over 4–8 weeks
- Impact: Forecasting goal from his profile

---

**Document prepared for:** Ahmed Ali, Senior Financial Analyst  
**Date:** January 31, 2026  
**Next action:** Confirm study start date (Feb 3); complete technical setup by Feb 2  
**Learning coach:** [Coach name/contact]  
**Weekly checkpoint calls:** Fridays 1 PM (15–20 min each)