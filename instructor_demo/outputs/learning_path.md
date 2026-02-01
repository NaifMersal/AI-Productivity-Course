# SEQUENTIAL LEARNING PATH: Python + Pandas for Month-End Close Automation
**Learner:** Ahmed Ali | **Timeline:** 8 weeks (3 hrs/week) | **Goal:** Automate GL Consolidation with Pandas  
**Last Updated:** Jan 31, 2026

---

## Overview: 4-Phase Learning Architecture

This learning path is **sequenced for maximum transfer** of Ahmed's VBA knowledge to Python, with each phase building on the previous. The progression moves from **foundational concepts** → **library mastery** → **financial automation** → **production readiness**.

```
Phase 1: Python Foundations (Weeks 1–2, 6 hrs)
    ↓
Phase 2: Pandas Essentials (Weeks 3–4, 6 hrs)
    ↓
Phase 3: Financial Automation (Weeks 5–7, 10 hrs)
    ↓
Phase 4: Refinement & Production (Week 8, 2 hrs)
```

---

## PHASE 1: Python Foundations (Weeks 1–2)
**Duration:** 6 hours total (3 hours/week)  
**Prerequisite:** None (Ahmed already has VBA experience)  
**Goal:** Build muscle memory for Python syntax; understand how Python "thinks" differently from Excel VBA

### Why This Phase Matters
Ahmed knows *how to program*—he's written complex VBA macros for 7 years. Phase 1 isn't about teaching programming; it's about translating his mental model from VBA to Python. He'll learn "Python is just VBA with different syntax."

---

### Phase 1 Sub-Skills Matrix

| **Sub-Skill** | **What Ahmed Needs to Learn** | **VBA Parallel** | **Depth** | **Time** | **Deliverable** |
|---|---|---|---|---|---|
| **1.1: Environment Setup** | Install Python, IDE (VS Code or PyCharm), run first script | Creating a new Excel workbook | Quick reference | 0.5 hrs | Python installed; "Hello World" script runs |
| **1.2: Data Types & Variables** | Integers, floats, strings, booleans; dynamic typing; variable naming | Dim x As Integer, s As String | Foundational | 1 hr | Write 5 scripts assigning variables & printing them |
| **1.3: String Manipulation** | Concatenation, methods (.upper(), .split(), .strip()), f-strings | Excel TEXT() & CONCATENATE() | Intermediate | 1 hr | Parse a GL account code string; extract cost center |
| **1.4: Lists & Loops** | Create lists, append items, for/while loops, range() | ReDim arrays, For i = 1 To lastRow | Foundational | 1.5 hrs | Loop through 10 GL accounts; filter by cost center |
| **1.5: Conditional Logic** | If/elif/else statements, boolean operators (and, or, not) | If condition Then / Else | Foundational | 0.5 hrs | Compare GL variance; identify >5% outliers |
| **1.6: Functions & Modules** | Define functions, parameters, return values, code reusability | Function myFunc(param1, param2) As Variant | Foundational | 1.5 hrs | Write 2 reusable functions (e.g., parse_account_code, calc_variance) |

### Phase 1 Learning Sequence

**Week 1 (3 hours)**
1. **1.5 hrs: Data Types, Variables & Output**
   - Watch: Real Python "Variables" tutorial (20 min)
   - Do: "Automate the Boring Stuff" Ch. 1 (data types, 30 min)
   - Practice: Write 3 scripts that assign & print GL account info (15 min)
   - Checkpoint: Understand `print()`, variable naming, string concatenation

2. **1.5 hrs: Loops & Conditionals**
   - Watch: Real Python "For Loops" & "If Statements" (30 min)
   - Do: Build a GL account filter script—loop through list, flag high variances (45 min)
   - Practice: Adapt script to filter by cost center (15 min)
   - Checkpoint: Comfortable with `for` loops & `if` logic

**Week 2 (3 hours)**
1. **1.5 hrs: String Manipulation & Functions**
   - Watch: Real Python "Strings" & "Functions" (30 min)
   - Do: Write function `extract_cost_center(account_code)` that parses GL codes (30 min)
   - Practice: Test function with 10 different GL account formats (20 min)
   - Checkpoint: Functions feel natural; understand parameters & return values

2. **1.5 hrs: Phase 1 Capstone**
   - **Mini-Project:** Consolidate a small GL dataset by cost center
     - Read hardcoded list of 20 GL transactions: `[{account: "1010-CC001", amount: 5000, variance: 2.3}, ...]`
     - Loop through; group by cost center
     - Filter variances > 5%; print summary report
   - Checkpoint: Script runs end-to-end; outputs correct consolidation

### Phase 1 Resources

| **Resource** | **Topics Covered** | **Duration** | **Why It's Chosen** |
|---|---|---|---|
| **Real Python: Python Basics** (Free) | Variables, types, strings, loops, conditionals | 4–5 hrs (partial) | Excellent explanations; no fluff; code-along friendly |
| **"Automate the Boring Stuff" Ch. 1–2** (Free online) | Data types, variables, print, input, strings | 3 hrs | Cookbook style; practical examples Ahmed can relate to |
| **DataCamp: Python Fundamentals** (Free tier, $40 upgrade) | Functions, loops, logic, debugging | 3 hrs | Interactive exercises; immediate feedback |
| **YouTube: Corey Schafer Python Tutorials** (Free) | Foundations; clear, patient explanations | 2–3 hrs (selective) | VBA learners praise his clarity; great for visual learners |

### Phase 1 Success Criteria

✅ Ahmed can write a Python script that:
- Defines variables and prints output without syntax errors
- Loops through a list of 20+ items and filters based on a condition (e.g., variance > 5%)
- Creates a reusable function that takes a GL account code as input, extracts cost center, and returns it
- Outputs a consolidation summary (total by cost center) to the console
- Understands why "Python is indentation-sensitive" (unlike VBA braces)

✅ Confidence checkpoint: Ahmed feels "I can read & write Python as naturally as VBA"

---

## PHASE 2: Pandas Essentials (Weeks 3–4)
**Duration:** 6 hours total (3 hours/week)  
**Prerequisite:** Phase 1 complete (comfort with Python syntax)  
**Goal:** Master Pandas DataFrames as the core data structure; read, filter, group, aggregate real GL data

### Why This Phase Matters
Phase 2 is the **most critical phase**. Pandas is a 80% of the month-end automation solution. Once Ahmed is fluent with DataFrames, everything else is "just pandas + financial logic."

Key insight: Pandas DataFrames are conceptually similar to Excel tables or SAP GL extracts—Ahmed already understands the *mental model*. He just needs to learn the pandas *syntax*.

---

### Phase 2 Sub-Skills Matrix

| **Sub-Skill** | **What Ahmed Needs to Learn** | **Excel/SAP Parallel** | **Depth** | **Time** | **Deliverable** |
|---|---|---|---|---|---|
| **2.1: DataFrame Basics** | Create DataFrames; understand structure (rows, cols, indices); `.head()`, `.shape`, `.info()` | Excel table structure; ROWS() & COLUMNS() functions | Foundational | 1 hr | Load GL sample data; explore structure with `.info()` |
| **2.2: Reading Data** | Read CSV, Excel (.xlsx), JSON; handle headers, data types, missing values | SAP export to CSV; Excel IMPORTDATA | Foundational | 1 hr | Read his actual GL export from SAP; confirm 10K+ rows loaded correctly |
| **2.3: Filtering & Selection** | Boolean indexing, .loc[], .iloc[], .query(); filter rows by condition | Excel AutoFilter; FILTER() function | Intermediate | 1.5 hrs | Filter GL by cost center, date range, amount threshold |
| **2.4: Grouping & Aggregation** | .groupby(), .sum(), .mean(), .count(), .agg(); multi-level grouping | Excel Pivot Table | Intermediate | 1.5 hrs | Group GL by account & cost center; sum amounts; calculate variance |
| **2.5: Joining & Merging** | .merge(), .join(), .concat(); left/inner/outer joins; combine GL + CoA | VLOOKUP, INDEX/MATCH, consolidation logic | Advanced | 0.5 hrs | Merge GL data with Chart of Accounts (CoA) to enrich account names |
| **2.6: Writing Output** | Export to CSV, Excel, JSON; format headers; add index control | Excel export; EXPORT functions | Intermediate | 0.5 hrs | Write consolidated GL summary to Excel with proper formatting |

### Phase 2 Learning Sequence

**Week 3 (3 hours)**
1. **1.5 hrs: DataFrame Fundamentals**
   - Watch: Real Python "Intro to Pandas" (30 min)
   - Do: "Automate the Boring Stuff" Ch. on Pandas or Real Python Pandas tutorial (30 min)
   - Practice: Load sample GL CSV; explore with `.info()`, `.head()`, `.describe()` (20 min)
   - Checkpoint: Understand DataFrame structure; feel comfortable printing rows & columns

2. **1.5 hrs: Reading & Exploring Real Data**
   - Get actual GL export from SAP (or anonymized sample)
   - Write script to read GL CSV with pandas: `df = pd.read_csv('GL_Jan2026.csv')`
   - Explore: `print(df.head(10))`, `print(df.dtypes)`, `print(df.shape)`
   - **Mini-checkpoint:** Real GL data loads; 10K+ rows visible; column names parsed correctly

**Week 4 (3 hours)**
1. **1 hr: Filtering & Selection**
   - Watch: Real Python "Selecting Data" tutorial (20 min)
   - Do: Filter GL by cost center, date range (30 min)
   - Practice: Write 3 filter queries (e.g., "Show all GL for CC001 > $10K") (10 min)
   - Checkpoint: Boolean indexing feels intuitive; understand `.loc[]` vs `.iloc[]`

2. **1 hr: Grouping & Aggregation**
   - Watch: Real Python "GroupBy" tutorial (20 min)
   - Do: Group GL by account & cost center; sum amounts; calculate total variance (30 min)
   - Practice: Modify grouping to match his actual month-end consolidation structure (10 min)
   - Checkpoint: Pivot table → Pandas groupby translation is clear

3. **1 hr: Phase 2 Capstone**
   - **Mini-Project:** Consolidate actual SAP GL export
     - Read 10K+ row GL dataset from CSV
     - Filter out intercompany transactions (if applicable)
     - Group by: Cost Center + Account Code
     - Aggregate: Sum(Amount), Count(Transactions), Variance from prior month
     - Export to Excel with summary sheet + detail sheet
   - Checkpoint: Output matches manual consolidation; script runs in <2 min

### Phase 2 Resources

| **Resource** | **Topics Covered** | **Duration** | **Why It's Chosen** |
|---|---|---|---|
| **Real Python: Pandas DataFrames** (Free articles) | DataFrame basics, filtering, grouping, merging | 8–10 hrs (partial) | High-quality; no corporate jargon; finance-friendly examples available |
| **DataCamp: Pandas Fundamentals Track** ($40–300/year) | Complete pandas curriculum; interactive exercises; finance focus available | 6–8 hrs | Best overall for Ahmed: cookbook style, real datasets, immediate feedback |
| **"Python for Data Analysis" by Wes McKinney (Pandas Author)** (Free chapters online / $50 book) | Deep dive on pandas design & best practices | 5+ hrs | Ultimate reference; overkill for 8-week goal but excellent for reference |
| **Kaggle Pandas Tutorials** (Free) | Practical pandas with real datasets | 4–6 hrs | Finance datasets available; learn by doing |
| **LinkedIn Learning: Pandas Essential Training** ($30–40/month or free via company) | Structured pandas curriculum; short modules | 3–4 hrs | Perfect for time-constrained learners; on-demand access |

### Phase 2 Success Criteria

✅ Ahmed can:
- Load his actual SAP GL export (10K+ rows) into a Pandas DataFrame without errors
- Explore the DataFrame structure: row count, column names, data types, null values
- Filter GL to show only transactions for a specific cost center, date range, or amount threshold
- Group GL by Account Code + Cost Center and calculate total amount, transaction count, and variance
- Merge GL data with a Chart of Accounts lookup table to enrich account names
- Export consolidated results to Excel with two sheets: summary (aggregated) + detail (filtered)
- Understand why a Pandas pivot table is equivalent to an Excel Pivot Table

✅ Confidence checkpoint: Ahmed thinks "Pandas is just Excel Pivot Tables + filtering in code form"

---

## PHASE 3: Financial Automation (Weeks 5–7)
**Duration:** 10 hours total (avg. 3+ hrs/week)  
**Prerequisite:** Phase 1 & 2 complete (Python syntax + Pandas fluency)  
**Goal:** Build working automation for month-end close; apply financial logic; handle real-world GL edge cases

### Why This Phase Matters
Phases 1 & 2 are *tools*. Phase 3 is *application*. Ahmed now builds the actual month-end close script that will save him 2–3 hours every month. This is where practice becomes production.

The focus here is less on learning new syntax, more on:
- Combining Pandas skills with financial consolidation logic
- Handling data quality issues (missing accounts, duplicate entries, formatting errors)
- Automating variance calculations (the core output of his MBR)
- Adding error handling so the script doesn't break mid-month

---

### Phase 3 Sub-Skills Matrix

| **Sub-Skill** | **What Ahmed Needs to Learn** | **Financial Context** | **Depth** | **Time** | **Deliverable** |
|---|---|---|---|---|---|
| **3.1: Data Validation & Cleaning** | Check for missing values, duplicates, data type mismatches; handle edge cases | GL account code validation; amount reasonableness checks | Intermediate | 1.5 hrs | Script validates GL export (10K rows) for missing cost center, invalid amounts |
| **3.2: Consolidation Logic** | Multi-level grouping; handling intercompany eliminations; rollup structures | Month-end consolidation by cost center, account, sub-entity | Advanced | 2 hrs | Consolidate GL by CC + Account + SubEntity; handle intercompany eliminations |
| **3.3: Variance Calculation** | Prior month comparison; threshold flagging; trend analysis | Variance = Current - Prior; Flag if >5% or >$X threshold | Intermediate | 1.5 hrs | Calculate variance vs. prior month; flag >5% variance for MBR review |
| **3.4: Error Handling & Logging** | Try/except blocks; log successes/failures; alerts for data issues | Graceful handling of missing GL accounts, malformed data | Intermediate | 1.5 hrs | Script logs all errors; alerts on data quality issues; doesn't crash mid-run |
| **3.5: Output Formatting** | Excel sheets with proper headers, currency formatting, summary statistics | MBR deck appearance: clean headers, totals, nice formatting | Intermediate | 1 hr | Export consolidated GL to Excel with formatted summary sheet |
| **3.6: Modular Code Structure** | Split script into functions; reusable components for different GL periods | Separate concerns: load → validate → consolidate → export | Intermediate | 1.5 hrs | Refactor monolithic script into 4–5 reusable functions |
| **3.7: Testing & Validation** | Compare automation output vs. manual consolidation; verify calculations | Spot-check totals, variances, account rolls; validate 100 sample rows | Intermediate | 1 hr | Run side-by-side comparison: automation vs. manual; confirm match |

### Phase 3 Learning Sequence

**Week 5 (3.5 hours)**
1. **1.5 hrs: Data Validation & Consolidation Logic**
   - Lesson: Real Python "Data Cleaning with Pandas" or DataCamp equivalent (30 min)
   - Do: Build validation logic—check GL for missing cost center, invalid amounts (45 min)
   - Practice: Add logic to flag orphaned GL accounts (not in CoA) (15 min)
   - Checkpoint: Script catches data quality issues before consolidation

2. **2 hrs: Multi-Level Consolidation & Eliminations**
   - Lesson: None (Ahmed already knows the business logic; just need pandas syntax)
   - Do: Build consolidation for CC + Account + SubEntity; add intercompany elimination logic (90 min)
   - Practice: Test against real GL data; verify totals match SAP manual consolidation (30 min)
   - Checkpoint: Consolidation output matches expected totals within $0 (exact)

**Week 6 (3.5 hours)**
1. **1.5 hrs: Variance Calculation & Flagging**
   - Lesson: Simple variance = Current - Prior (Ahmed knows this already)
   - Do: Load prior month GL; merge with current month; calculate variance; flag >5% (45 min)
   - Practice: Enhance to show trend (3-month variance, YTD variance) (30 min)
   - Checkpoint: Variance column matches MBR calculations

2. **2 hrs: Error Handling & Modular Code**
   - Lesson: Python "Try/Except" & error handling (20 min)
   - Do: Add error handling to script; split into functions (load_gl, validate, consolidate, export) (75 min)
   - Practice: Test each function independently; test integration (25 min)
   - Checkpoint: Script handles missing files, corrupt data gracefully without crashing

**Week 7 (3 hours)**
1. **1.5 hrs: Output Formatting & Logging**
   - Lesson: Pandas styling, Excel formatting with openpyxl or xlsxwriter (20 min)
   - Do: Export consolidated GL to Excel with formatted headers, currency format, bold totals (50 min)
   - Practice: Add logging to track script execution (timestamps, row counts, errors) (20 min)
   - Checkpoint: Excel output looks professional; readable as-is without further editing

2. **1.5 hrs: Phase 3 Capstone & Testing**
   - **Major Project:** End-to-End Month-End Automation
     - Load January 2026 GL from SAP (real or sample)
     - Validate data (missing cost centers, amounts, accounts)
     - Consolidate by CC + Account; calculate variance vs. December
     - Flag variances > 5% for review
     - Export consolidated GL + summary + variance report to Excel
     - Log all steps (rows loaded, validations passed, errors caught)
   - **Validation:**
     - Compare script output vs. Ahmed's manual consolidation from 3 months ago
     - Verify totals match to the dollar
     - Ensure output is production-ready (no "temp" values, clean formatting)
   - Checkpoint: Script is 95% of final product; ready for Week 8 polish

### Phase 3 Resources

| **Resource** | **Topics Covered** | **Why It's Chosen** |
|---|---|---|
| **Real Python: Error Handling** (Free) | Try/except, exception types, logging | Clear, practical examples |
| **DataCamp: Data Cleaning with Pandas** | Validation, handling missing data, duplicates | Interactive; finance examples |
| **Pandas Documentation: I/O & Formatting** (Free online) | Excel export, styling, openpyxl integration | Official reference; code examples |
| **Openpyxl or XlsxWriter Docs** (Free online) | Excel cell formatting, conditional formatting, headers | For polishing output |
| **1-on-1 Tutor Session (Optional)** | Custom guidance on consolidation logic, testing approach | Fast-track blockers; code review |

### Phase 3 Success Criteria

✅ Ahmed has a **working, production-ready script** that:
- Loads GL export from SAP (handles file not found, format errors gracefully)
- Validates GL data (flags missing cost center, invalid amounts, unknown accounts)
- Consolidates GL by CC + Account + SubEntity with intercompany elimination logic
- Calculates variance vs. prior month and flags >5% outliers
- Exports to Excel: summary sheet (totals by CC/Account) + detail sheet (all transactions) + variance sheet
- Includes proper error handling (try/except) so it doesn't crash mid-execution
- Logs all execution steps to console or file (rows loaded, validations, time taken)
- Runs in <2 minutes for 10K+ row GL extract

✅ Testing checkpoint: Script output **matches** Ahmed's manual January consolidation (from memory or records) within $0 tolerance

✅ Confidence checkpoint: Ahmed thinks "I could run this script on the 1st of every month and have month-end close 80% done"

---

## PHASE 4: Refinement & Production Readiness (Week 8)
**Duration:** 2 hours total  
**Prerequisite:** Phase 3 complete (working automation script)  
**Goal:** Polish code; add documentation; prepare for production use and transfer to colleagues

### Why This Phase Matters
A working script is not a *product*. Phase 4 transforms the working script into something a colleague (or future Ahmed, 6 months from now) can run and maintain. This includes:
- Code comments & documentation
- User guide (how to run, what to do if it breaks)
- Scheduling the script to run automatically each month
- Knowledge transfer so someone else can maintain it

---

### Phase 4 Sub-Skills Matrix

| **Sub-Skill** | **What Ahmed Needs to Learn** | **Context** | **Depth** | **Time** | **Deliverable** |
|---|---|---|---|---|---|
| **4.1: Code Documentation** | Docstrings, comments, README file; explain logic in plain English | Why each section exists; what inputs/outputs are | Light | 0.5 hrs | Fully commented script; README with usage instructions |
| **4.2: User Guide** | Step-by-step instructions for running script; troubleshooting guide | "Place GL export here"; "If error X happens, do Y" | Light | 0.5 hrs | 1-page user guide (for non-technical colleague) |
| **4.3: Scheduling & Automation** | Windows Task Scheduler or cron job; automated monthly execution | Script runs automatically on 1st of month | Light | 0.5 hrs | Scheduled job configured; runs unattended |
| **4.4: Code Review & Cleanup** | Remove debugging code, unused variables; final polish | Professional appearance; no "temp" or "test" code | Light | 0.5 hrs | Clean, submission-ready script |

### Phase 4 Learning Sequence

**Week 8 (2 hours)**

1. **0.5 hrs: Code Documentation & Comments**
   - Add docstrings to each function: `def consolidate_gl(df, period): """Consolidate GL by cost center & account."""`
   - Add inline comments explaining complex logic (variance calculation, elimination rules)
   - Create README.md with: purpose, prerequisites, how to run, example output
   - Checkpoint: Any colleague can read & understand the script

2. **0.5 hrs: User Guide & Troubleshooting**
   - Write simple 1-page guide: "How to Run Month-End Close Automation"
   - Include: file locations, expected runtime, what to do if script fails, how to interpret output
   - Add FAQ: "What if I get an error about missing cost center?" → "Check GL export; ensure all CCs are populated"
   - Checkpoint: Non-technical colleague can follow the guide

3. **0.5 hrs: Scheduling & Automation**
   - Lesson: Windows Task Scheduler (if company uses Windows) or cron (if Linux/Mac)
   - Do: Set up scheduled job to run Python script on 1st of each month at 6 AM
   - Test: Confirm script runs unattended; output appears in expected folder
   - Checkpoint: Script runs automatically; Ahmed gets email confirmation on 1st of month

4. **0.5 hrs: Final Code Review & Submission**
   - Remove any debugging code (print statements, test data)
   - Rename variables to be self-documenting (`variance_pct` not `v`)
   - Check for unused imports, dead code
   - Final test: Run script end-to-end one more time
   - Checkpoint: Script is production-ready; ready to deploy

### Phase 4 Resources

| **Resource** | **Topics Covered** | **Why It's Chosen** |
|---|---|---|
| **PEP 257: Python Docstring Conventions** (Free online) | How to write docstrings | Official Python standard; easy reference |
| **Real Python: Writing Docstrings** (Free) | Practical docstring examples | Clear, practical guidance |
| **Windows Task Scheduler Tutorial** or **Linux Cron Tutorial** (Free online) | Automated script execution | OS-specific; easy setup guides available |

### Phase 4 Success Criteria

✅ Ahmed's script is **production-ready**:
- Every function has a docstring explaining inputs, outputs, and purpose
- Complex logic (variance calculation, eliminations) has inline comments
- README.md file explains: what script does, how to use it, where to place GL export, what to expect
- User guide is simple enough for a non-technical colleague to follow
- Script runs automatically on 1st of month via scheduled job (Task Scheduler or cron)
- All test/debug code removed; variable names are clear and self-documenting
- Final test run: script executes cleanly from start to finish, outputs clean Excel file

✅ Confidence checkpoint: Ahmed can hand the script to a colleague and say "You can run this every month without my help"

---

## SUMMARY: 4-Phase Learning Path At a Glance

| **Phase** | **Duration** | **Focus** | **Key Learning** | **Deliverable** |
|---|---|---|---|---|
| **Phase 1: Python Foundations** | 2 weeks, 6 hrs | Syntax & mental model | Variables, loops, functions, conditionals | Mini-project: Consolidate hardcoded GL list by cost center |
| **Phase 2: Pandas Essentials** | 2 weeks, 6 hrs | DataFrame mastery | Read data, filter, group, aggregate, merge, write | Mini-project: Load & consolidate 10K-row SAP GL export to Excel |
| **Phase 3: Financial Automation** | 3 weeks, 10 hrs | Production automation | Validation, consolidation logic, variance, error handling, logging | Major project: End-to-end month-end close script (working prototype) |
| **Phase 4: Refinement & Production** | 1 week, 2 hrs | Polish & transfer | Documentation, scheduling, cleanup | Production-ready script + user guide; scheduled job set up |
| **TOTAL** | **8 weeks, 24 hrs** | **From zero Python → production automation** | **Translate VBA expertise to Python + Pandas** | **Automated month-end close; 2–3 hours saved every month** |

---

## Cross-Phase Themes

### 1. **Leverage VBA Knowledge at Every Step**
- Week 1: "This `for` loop in Python is like `For i = 1 To lastRow` in VBA"
- Week 3: "A Pandas DataFrame is like an Excel table; groupby is like a Pivot Table"
- Week 5: "Error handling with `try/except` is like `On Error Resume Next` in VBA"

### 2. **Real Data, Not Toy Examples**
- Week 1: Use hardcoded GL account list (realistic format)
- Week 3: Load actual SAP GL export (10K+ rows)
- Week 5: Consolidate real January GL; compare to prior manual consolidation
- Week 8: Schedule the actual script for production use

### 3. **Incremental Complexity**
- Week 1: 20 GL accounts (hardcoded list)
- Week 3: 10K+ GL accounts (CSV export)
- Week 5: 10K+ GL accounts + intercompany logic + variance + validation
- Week 8: Production script with logging, error handling, scheduling

### 4. **Testing & Validation**
Each phase includes a checkpoint comparing automation output to manual/expected results:
- Phase 1: Output matches expected list filter (logic is correct)
- Phase 2: Consolidation totals match prior month manual calculation
- Phase 3: Side-by-side comparison: automation vs. manual; must match dollar-for-dollar
- Phase 4: Script runs unattended; output is production-ready

---

## Pre-Phase 1: Setup Checklist (Do This First!)

Before Ahmed starts Phase 1, complete these setup tasks (1–2 hours):

**Technical Setup:**
- [ ] Install Python 3.10+ from python.org
- [ ] Install VS Code or PyCharm Community Edition (IDE)
- [ ] Create project folder: `C:\Users\Ahmed\month_end_automation\`
- [ ] Install pandas: `pip install pandas openpyxl`
- [ ] Test: Run `python -c "import pandas; print(pandas.__version__)"` → Should print version number
- [ ] Get sample GL export from SAP (anonymized if needed); place in project folder

**Knowledge Setup:**
- [ ] Get copy of Ahmed's current month-end close procedure (how he consolidates manually)
- [ ] Identify: what are the consolidation rules? (intercompany eliminations? cost center mappings?)
- [ ] Identify: what does final MBR output look like? (which sheets, which columns, what formatting?)
- [ ] Document: prior month GL totals (for variance testing in Week 3)

**Time Setup:**
- [ ] Block calendar: 3 hrs/week, same time each week (e.g., Wed 2–5 PM mid-month)
- [ ] Avoid: Weeks 1, 3, 5 month-end crunch (Days 1–5 of month)
- [ ] Plan: Weekly 15-min checkpoint calls with learning coach

---

## Phase-by-Phase Checkpoint Calls

| **Week** | **Duration** | **Focus** | **Questions** |
|---|---|---|---|
| **End of Week 2** | 15 min | Phase 1 mastery | "Show me your consolidation script. Can you explain each function? Any blockers?" |
| **End of Week 4** | 15 min | Phase 2 mastery | "Load your GL CSV. Group by cost center. Show me output. Does it match expected?" |
| **End of Week 6** | 20 min | Phase 3 progress | "Show me your consolidation + variance script. Does output match manual consolidation?" |
| **End of Week 8** | 20 min | Production readiness | "Walk me through script + user guide. Is it ready for a colleague to run?" |

---

## How to Use This Learning Path

### For Ahmed:
1. Read each phase's overview first (why this phase matters)
2. Work through sub-skills in order—don't skip ahead
3. Use the learning resources suggested (Real Python, DataCamp, etc.)
4. After each sub-skill, tackle the mini-project to apply it
5. At end of each phase, complete the success criteria checklist
6. If stuck, refer to the VBA parallel ("In VBA, this is like...")

### For Learning Coach / Manager:
1. Assign phase-by-phase (don't overload with all 4 phases at once)
2. Review mini-projects at end of each phase
3. Hold weekly checkpoint calls (15–20 min) to unblock issues
4. If Ahmed falls behind: extend phase, don't compress—quality over speed
5. Celebrate wins: "You just automated a task that took 3 hours; you saved 12 hours this month!"

---

## Realistic Timeline Adjustments

This path assumes **ideal conditions**: 3 hrs/week uninterrupted mid-month, no blockers, learning at expected pace.

**If Ahmed falls behind:**
- Week 1–2 extend to Weeks 1–3 (month-end crunch may interrupt)
- Move Phase 2 start to Week 4 (not Week 3)
- Recommend extending overall timeline to **10–12 weeks** instead of 8

**If Ahmed accelerates:**
- Week 3: Can do both "filtering" and "grouping" in same week (some overlap)
- Week 5: Can add SQL basics (querying GL directly from SAP) as stretch goal

**Red flags indicating extended timeline needed:**
- Week 2 checkpoint: "I don't feel comfortable writing functions yet"
- Week 4 checkpoint: "Groupby still confuses me; the syntax is weird"
- Week 6 checkpoint: "My consolidation output doesn't match; I'm debugging"

**Response:** Extend phase by 1–2 weeks. Better to spend 9–10 weeks and have solid mastery than 8 weeks and shaky confidence.

---

## Success Metrics (End of 8 Weeks)

Ahmed will have achieved the learning goal if:

1. ✅ **Automation Script:** He has a working Python script that automates 60–80% of his month-end close (GL consolidation, variance calculation, Excel export)
2. ✅ **Time Savings:** Script runs in <2 minutes vs. his 2–3 hour manual process (10x faster)
3. ✅ **Accuracy:** Output matches manual consolidation dollar-for-dollar (verified in Phase 3)
4. ✅ **Usability:** A colleague can run the script following the 1-page user guide without his help
5. ✅ **Confidence:** Ahmed can read, write, and debug Python code; feels comfortable with pandas; can modify script for future use cases
6. ✅ **Production Ready:** Script has error handling, logging, scheduling, and documentation

**Bonus (Stretch) Goals:**
- Add SQL basics to query GL directly from SAP (skip CSV export step)
- Add predictive modeling for variance forecasting (his stated secondary goal)
- Train a colleague to maintain the script

---

## Post-8-Week Learning Path (Future)

Once Phase 4 is complete, Ahmed can pursue secondary goals:

**Month 3 (Weeks 9–12):**
- Learn SQL basics to query GL directly from SAP ERP
- Eliminate the CSV export step; read GL directly into Python
- Estimated effort: 4–6 hours over 4 weeks

**Month 4+ (Weeks 13+):**
- Learn NumPy + scikit-learn for predictive variance modeling
- Build ML model to forecast month-end variance (his stated secondary priority)
- Estimated effort: 12–16 hours over 4–8 weeks
- Impact: Forecast variance 2–3 weeks ahead instead of month-end surprise

---

**Document prepared for:** Ahmed Ali, Senior Financial Analyst  
**Date:** Jan 31, 2026  
**Next action:** Confirm Phase 1 start date; ensure technical setup is complete; schedule Week 2 checkpoint