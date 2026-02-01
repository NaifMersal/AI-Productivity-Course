# PYTHON LEARNING PLAN FOR MONTH-END CLOSE AUTOMATION
**For:** Ahmed Ali, Senior Financial Analyst  
**Goal:** Automate SAP data consolidation using Python & pandas  
**Timeline:** 12 weeks (Feb–Apr 2026)  
**Time Commitment:** 3 hours/week (mid-month); pause during month-end crunch

---

## OVERVIEW
This plan takes you from "Python novice" → "able to replace your Excel consolidation macro with a Python script" in 12 weeks. Every lesson maps to a real task in your month-end close workflow.

---

## PHASE 1: FOUNDATIONS (Weeks 1–3)
**Goal:** Build Python syntax confidence + understand pandas basics  
**Time:** ~9 hours total (3 hrs/week)

### Week 1: Python Essentials for Finance People
**Why this order:** You know VBA already, so we'll use that as a bridge.

**Learn:**
- Variables, data types (int, float, string, datetime)
- Lists and dictionaries
- Basic loops and conditions
- Why Python > Excel for data work

**Cookbook Resources:**
- **Free:** DataCamp's "Introduction to Python" (2 hours) OR Codecademy's Python course
- **Paid:** LinkedIn Learning "Python for Finance" (intro section)
- **Your actual work:** Export a small SAP GL data sample; follow along with the course using YOUR data, not dummy examples

**Practical Task:**
Write 3 simple scripts that mimic what you do manually:
1. Read a CSV file (your GL export)
2. Add a calculated column (e.g., variance = actual – budget)
3. Print results to console

**Time:** 3 hours

---

### Week 2: Pandas Crash Course (The Game-Changer)
**Why:** Pandas does in 5 lines what takes you 50 lines of VBA.

**Learn:**
- DataFrames (think: Excel table in Python)
- Reading Excel/CSV files into pandas
- Selecting columns, filtering rows
- Basic aggregation (sum, count, average by department)
- Concatenating multiple data sources

**Cookbook Resources:**
- **Free:** Real Python's "Pandas DataFrames" tutorial
- **Paid:** DataCamp "Data Manipulation with pandas" (4–5 hour course)
- **YouTube:** Corey Schafer's "Pandas Tutorial" (very clear, 2 hrs)

**Practical Task:**
Recreate your month-end consolidation in pandas:
1. Load your 3–5 GL files from SAP
2. Stack them into one DataFrame
3. Filter to active accounts only
4. Aggregate by cost center and account
5. Compare to your current Excel output (they should match)

**Time:** 3 hours

---

### Week 3: Cleaning Real Data (The Missing 80%)
**Why:** Your SAP exports are messy. You need to handle that programmatically.

**Learn:**
- Handling missing values (NaN, blanks)
- Data type conversion (text to date, string to number)
- Removing duplicates
- Renaming columns
- Creating lookup tables (mapping cost center codes to names)

**Cookbook Resources:**
- Real Python's "Data Cleaning with Pandas"
- Kaggle's "Data Cleaning" micro-course
- Your SAP exports (the real teacher)

**Practical Task:**
Take a raw SAP GL export and build a cleaning script:
1. Remove header junk/footers
2. Convert date formats
3. Handle missing GL descriptions
4. Map cost center codes to cost center names
5. Flag any anomalies (zero balances, negative amounts that shouldn't be)

**Output:** A clean DataFrame ready for consolidation.

**Time:** 3 hours

**CHECKPOINT:** By end of Week 3, you should have a working script that mimics 50% of your current Excel macro. Test it on last month's data.

---

## PHASE 2: BUILD YOUR FIRST AUTOMATION (Weeks 4–8)
**Goal:** Replace your manual consolidation with a Python script  
**Time:** ~15 hours total

### Week 4–5: Building the Month-End Consolidation Script
**What you'll build:** A single Python script that does everything your Excel macro does (but faster, more reliable, auditable).

**Learn:**
- Writing functions (reusable code blocks)
- Reading from SAP exports
- Joining datasets (matching GL codes across files)
- Variance analysis (actual vs. budget)
- Exporting to Excel (for your CFO deck)

**Cookbook Structure:**
```
Input: 3 SAP GL files (Regions A, B, C)
├── Load & clean each file
├── Standardize columns
├── Stack into one master GL
├── Add cost center names
├── Calculate variances
├── Aggregate by cost center
└── Export to Excel
```

**Resources:**
- Real Python's "Reading and Writing Files with Pandas"
- Pandas documentation on `.merge()` (SQL-like joins)
- **Free tool:** Jupyter Notebook (cloud version: Google Colab)

**Practical Task:**
Build `consolidate_month_end.py`:
```python
# Pseudocode outline (you'll fill this in)
import pandas as pd

def load_region_data(file_path):
    df = pd.read_excel(file_path, sheet_name='GL')
    # Clean the data (from Week 3)
    return df

def consolidate_all_regions():
    region_a = load_region_data('RegionA_Jan2026.xlsx')
    region_b = load_region_data('RegionB_Jan2026.xlsx')
    region_c = load_region_data('RegionC_Jan2026.xlsx')
    
    master = pd.concat([region_a, region_b, region_c])
    # Add variance, etc.
    return master

if __name__ == '__main__':
    result = consolidate_all_regions()
    result.to_excel('Month_End_Consolidation.xlsx', index=False)
```

**Success Metric:** Your output matches your current Excel consolidation, but the script runs in <30 seconds instead of 15 minutes.

**Time:** 4 hours (Weeks 4–5)

---

### Week 6: Error Handling & Validation
**Why:** Your script needs to tell you when something went wrong (corrupt file, missing data, unexpected GL code).

**Learn:**
- Try/except blocks (when things go wrong)
- Data validation (ensure numbers are reasonable)
- Logging (save a record of what the script did)
- Testing your code

**Practical Task:**
Add error handling to your consolidation script:
1. What if a file is missing? Warn, not crash.
2. What if a GL balance is negative when it shouldn't be? Flag it.
3. What if actuals are 300% of budget? Raise an alert.
4. Create a log file so you know exactly what the script processed.

**Time:** 3 hours

---

### Week 7: Scheduling & Automation
**Goal:** Run your script automatically on the 1st of each month, no manual steps.

**Learn:**
- Task Scheduler (Windows) or cron (Mac/Linux)
- Or: Simple scheduling via Python (schedule library)
- Email notifications (send the output to your CFO)

**Practical Task:**
Set up your consolidation script to run automatically on Feb 1st, Mar 1st, etc. Receive a summary email with:
- "Consolidation complete: X accounts, Y cost centers"
- Any alerts/anomalies
- Link to the output file

**Time:** 2 hours

---

### Week 8: Documentation & Knowledge Transfer
**Why:** You want others to use this (and not call you every time it breaks).

**Learn:**
- Writing clear comments in code
- Creating a README file
- Basic troubleshooting guide

**Practical Task:**
Document your script for a junior analyst:
- How to run it
- What each section does
- Common errors & fixes
- Where to find SAP exports

**Time:** 2 hours

**CHECKPOINT:** By end of Week 8, you have a fully automated, documented month-end consolidation script running on schedule. This is your **MVP (Minimum Viable Product)**.

---

## PHASE 3: EXTEND & OPTIMIZE (Weeks 9–12)
**Goal:** Add revenue forecasting + optimize performance  
**Time:** ~6 hours total

### Week 9–10: Intro to Predictive Modeling (Secondary Goal)
**What you'll learn:** Basic forecasting for quarterly revenue variance

**Learn:**
- Time series basics (monthly trends)
- Simple exponential smoothing
- Linear regression (trend + seasonality)
- Why: Beats guessing; shows CFO your rigor

**Cookbook Resources:**
- StatQuest with Josh Starmer's "Time Series Forecasting" (YouTube)
- Real Python's "Forecasting with Pandas"
- Libraries: `statsmodels` (built-in forecasting)

**Practical Task:**
Build a simple revenue forecast:
1. Load 12–24 months of historical revenue
2. Visualize trends (matplotlib/seaborn)
3. Fit a simple trend line
4. Forecast next quarter
5. Compare forecast to actual (as months close)

**Time:** 3 hours

---

### Week 11: Performance Optimization
**If your script is slow:** Learn to speed it up.

**Learn:**
- Why some pandas code is slow
- `.apply()` vs. vectorization
- Reading large files efficiently

**Time:** 2 hours (only if needed)

---

### Week 12: Capstone + Next Steps
**Review & Plan:**
- Run through your entire workflow one more time
- Are there other Excel tasks you could automate?
- Plan next: SQL (connecting directly to SAP database)?

**Time:** 1 hour

---

## LEARNING RESOURCES & BUDGET BREAKDOWN
**Annual Budget:** $1,000

| Resource | Cost | Time | Priority |
|----------|------|------|----------|
| DataCamp (annual) | $300 | 15 hrs | HIGH |
| Real Python (membership) | $100/year | On-demand | HIGH |
| LinkedIn Learning (via company) | FREE | 5 hrs | MEDIUM |
| YouTube (free) | FREE | 5 hrs | HIGH |
| Google Colab (free) | FREE | - | HIGH |
| **Total Cost** | **~$400** | - | - |

**Remaining Budget:** $600 (save for SQL/database course next year)

---

## WEEKLY SCHEDULE TEMPLATE
**Mid-Month (Weeks 1–12):** Mon/Wed/Fri, 1 hour each (or 3 hours on Wed)

| Time Slot | Activity |
|-----------|----------|
| 30 min | Watch course video OR read tutorial |
| 90 min | Code along with your actual SAP data |
| 30 min | Troubleshoot + document what you learned |

**Month-End Crunch (Days 1–5):** Pause learning. Use the first week of each month as a "free week" — no required learning.

---

## MILESTONES & SUCCESS METRICS

| Milestone | Target Date | Success Criteria |
|-----------|-------------|-----------------|
| Basic Python fluency | Mid-Feb | Write a script that reads/filters/exports GL data |
| Pandas fundamentals | Late Feb | Consolidate 3 files in pandas; output matches Excel |
| Cleaning real data | Early Mar | Handle messy SAP exports without errors |
| **MVP: Automation running** | Mid-Mar | Your month-end script runs in <1 min; no manual steps |
| Error handling + logging | Late Mar | Script catches & reports issues; you get a log file |
| Scheduled & automated | Early Apr | Script runs on 1st of month; email notification works |
| Forecasting basics | Mid-Apr | Simple revenue forecast built; CFO gets it in MBR |

---

## RED FLAGS & HOW TO STAY ON TRACK

| Risk | Solution |
|------|----------|
| **"I'm too busy mid-month"** | Pause during crunch. Reschedule the 3 hours to the following week. |
| **"This is hard; I want to quit"** | Remember: you already know VBA. Python is just different syntax. Push through Week 2. |
| **"My SAP export format changed"** | Perfect teaching moment. This is exactly why you're automating — flexibility. |
| **"I don't know why my code isn't working"** | Use ChatGPT/Copilot with your actual error message. OR post on Stack Overflow. |
| **"Weeks 9–12 feel optional"** | They are optional if your main goal (month-end automation) is done. |

---

## FINAL NOTES FOR YOU

1. **Start Small:** Don't try to do everything. Weeks 1–8 give you 80% of the value. Weeks 9–12 are "nice-to-have."

2. **Use Real Data:** Every exercise should use your actual GL export, not dummy data. This keeps you motivated and makes the output immediately useful.

3. **You Already Know Half of This:** You've written VBA macros for 7 years. Python is just new syntax for the same logic. Lean on that.

4. **Copy-Paste is OK:** You don't need to memorize syntax. Copy recipes from Real Python or Stack Overflow and adapt them. That's what professionals do.

5. **Celebrate Week 3:** Once you've cleaned real SAP data in pandas, you've leveled up. The rest is scaling what you already know.

6. **By April, You'll Wonder:** "Why did I spend 7 years doing this in Excel?" Your team will thank you.

---

## NEXT STEP
Choose your learning platform:
- **DataCamp** (most structured, 2–3 hours/week)
- **Real Python** (best tutorials, self-paced)
- **YouTube** (free, but less structured)

Start Week 1 tomorrow. You've got 12 weeks. Let's automate your month-end close.