# 8-Week Python Automation Roadmap

## Month-End Close Automation

**Senior Financial Analyst**

### Program Overview

This roadmap converts Python fundamentals into working month-end close automation. No theory exercises—only recipes you'll use immediately in production.

| Duration | Weekly Time | Total Hours | Deliverable |
|----------|-------------|-------------|-------------|
| 8 weeks | 3 hours | 24 hours | Working Python automation script |

### Prerequisites

- Excel expertise: You know VLOOKUP, pivot tables, formulas
- VBA comfort: You can read and write basic macros
- Python basics: You understand variables, loops, functions (from earlier learning)
- Tools installed: Python 3.11+, VS Code, Git

---

## Week 1: Python for Excel Data (Read & Write)

### Goal

Replace manual CSV exports with Python scripts. Write clean data to Excel programmatically.

### Time Allocation

- Setup & install libraries: 30 min
- Read data from Excel: 1 hour
- Write formatted data to Excel: 1 hour
- Practice exercise: 30 min

### Recipe 1.1: Read Excel Data

Install pandas and openpyxl:

```bash
pip install pandas openpyxl
```

Code:

```python
import pandas as pd

df = pd.read_excel('GL_extract.xlsx', sheet_name='Raw')
print(df.head())
print(df.shape)
```

**What you get:** A DataFrame (like a pivot table) with all GL data. The shape tells you row count and columns. This replaces manually opening files.

### Recipe 1.2: Write Formatted Excel

Code:

```python
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Summary', index=False)
    ws = writer.sheets['Summary']
    for col in ws.columns:
        ws.column_dimensions[col[0].column_letter].width = 20
```

**What you get:** An Excel file where Python automatically sets column widths. No manual formatting.

### Deliverable

- Read your actual GL_extract.xlsx file
- Filter for one cost center
- Write to a new file with auto-width columns

---

## Week 2: Data Cleaning (Pandas Recipes)

### Goal

Handle messy GL data—blanks, duplicates, wrong date formats. Replaces manual Find & Replace.

### Time Allocation

- Handle null/blank cells: 45 min
- Remove duplicates: 30 min
- Fix date formats: 1 hour
- Practice: 15 min

### Recipe 2.1: Handle Blanks

Code:

```python
df = df.dropna(subset=['Account'])  # Remove rows with blank Account
df['Cost Center'] = df['Cost Center'].fillna(0)  # Fill blanks with 0
```

### Recipe 2.2: Remove Duplicates

Code:

```python
df = df.drop_duplicates(subset=['Date', 'Amount', 'Account'], keep='first')
```

### Recipe 2.3: Fix Date Formats

Code:

```python
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df['Month'] = df['Date'].dt.month
```

### Deliverable

Script that reads raw GL data, cleans it (removes blanks, duplicates, fixes dates), and exports clean file.

---

## Week 3: Joins & Lookups (Like VLOOKUP, Pandas-Style)

### Goal

Join GL data with chart of accounts. Merge GL with cost center descriptions. Much faster than VLOOKUPs.

### Time Allocation

- Inner joins: 1 hour
- Left/Right joins: 1 hour
- Multiple joins chain: 1 hour

### Recipe 3.1: Merge (VLOOKUP Replacement)

Code:

```python
coa = pd.read_excel('ChartOfAccounts.xlsx')
result = pd.merge(df, coa, left_on='Account', right_on='AcctNo', how='left')
print(result.head())
```

**What you get:** GL data now has account descriptions from the COA file. No VLOOKUP formula needed. Handles mismatches automatically.

### Recipe 3.2: Multiple Joins

Code:

```python
result = df.merge(coa, on='Account', how='left')
result = result.merge(cost_centers, on='CostCenter', how='left')
result = result.merge(regions, on='Region', how='left')
```

### Deliverable

Script that joins GL data with COA, cost centers, and regions. Output: single Excel file with all descriptions.

---

## Week 4: Aggregation & Summaries

### Goal

Create pivot-like summaries: GL by account, by cost center, by month. This is your first "real" month-end report.

### Time Allocation

- GroupBy basics: 1 hour
- Multi-level aggregations: 1 hour
- Pivot tables in code: 1 hour

### Recipe 4.1: Simple GroupBy

Code:

```python
summary = df.groupby('Account')['Amount'].sum().reset_index()
summary.columns = ['Account', 'Total']
print(summary)
```

**What you get:** One row per account with total amount. Like Excel's Subtotal function.

### Recipe 4.2: Multi-Level Summary

Code:

```python
summary = df.groupby(['Month', 'Account', 'CostCenter']).agg({
    'Amount': 'sum',
    'Count': 'count'
}).reset_index()
```

**What you get:** Totals by month, account, AND cost center in one command. No manual sorting needed.

### Recipe 4.3: Pivot Table Code

Code:

```python
pivot = df.pivot_table(values='Amount', index='Account', columns='Month', aggfunc='sum', fill_value=0)
```

**What you get:** A pivot table where rows = accounts, columns = months, values = totals. Identical to Excel pivot table.

### Deliverable

Script that creates 3 Excel sheets: (1) GL by account, (2) GL by cost center, (3) pivot table of amounts by month & account.

---

## Week 5: Validation & Reconciliation Rules

### Goal

Build reconciliation checks: verify GL total matches subledger. Flag unmatched records. Replaces manual Compare spreadsheets.

### Time Allocation

- Simple filters & conditions: 45 min
- Reconciliation matching: 1 hour 15 min
- Exception reporting: 45 min

### Recipe 5.1: Validation Filters

Code:

```python
# Flag negative amounts
df['is_negative'] = df['Amount'] < 0

# Find amounts > $1M
df['large_amount'] = df['Amount'].abs() > 1000000

# Export exceptions
exceptions = df[df['large_amount']]
exceptions.to_excel('exceptions.xlsx')
```

### Recipe 5.2: Reconciliation

Code:

```python
gl_total = df['Amount'].sum()
subledger_total = subledger['Amount'].sum()

if gl_total == subledger_total:
    print('MATCH')
else:
    diff = gl_total - subledger_total
    print(f'VARIANCE: ${diff:,.2f}')
```

### Recipe 5.3: Find Unmatched Records

Code:

```python
matched = df.merge(subledger[['ID']], on='ID', how='inner')
unmatched = df[~df['ID'].isin(matched['ID'])]
print(f'Unmatched records: {len(unmatched)}')
```

### Deliverable

Script that compares GL to subledger, shows variance, exports unmatched and large transactions to separate sheets.

---

## Week 6: Integrating Everything (Pipeline)

### Goal

Combine weeks 1–5 into one script that runs start-to-finish: read GL, clean, join, summarize, validate, export all reports.

### Time Allocation

- Refactor recipes into functions: 1 hour
- Build pipeline structure: 1 hour
- Test & debug: 1 hour

### Recipe 6.1: Function Structure

Code:

```python
def load_data(filepath):
    return pd.read_excel(filepath)

def clean_data(df):
    df = df.dropna(subset=['Account'])
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def summarize_by_account(df):
    return df.groupby('Account')['Amount'].sum()

def validate_reconciliation(gl, subledger):
    diff = gl['Amount'].sum() - subledger['Amount'].sum()
    return diff == 0
```

### Recipe 6.2: Main Script

Code:

```python
if __name__ == '__main__':
    # Load
    gl = load_data('GL_extract.xlsx')
    subledger = load_data('subledger.xlsx')
    
    # Clean
    gl = clean_data(gl)
    subledger = clean_data(subledger)
    
    # Reconcile
    match = validate_reconciliation(gl, subledger)
    print(f'Reconciliation: {"PASS" if match else "FAIL"}')
    
    # Summarize & export
    summary = summarize_by_account(gl)
    summary.to_excel('month_end_report.xlsx')
```

### Deliverable

Single Python script that reads inputs, executes all cleaning/joining/validation steps, outputs month-end report with validation status.

---

## Week 7: Error Handling & Robustness

### Goal

Make the script production-ready: handle missing files, bad data, date errors gracefully. Add logging so you know what went wrong.

### Time Allocation

- Try/except patterns: 1 hour
- Logging setup: 1 hour
- Test failure scenarios: 1 hour

### Recipe 7.1: Error Handling

Code:

```python
import logging

logging.basicConfig(filename='month_end.log', level=logging.INFO)

try:
    gl = pd.read_excel('GL_extract.xlsx')
except FileNotFoundError:
    logging.error('GL_extract.xlsx not found')
    raise

try:
    gl['Date'] = pd.to_datetime(gl['Date'])
except Exception as e:
    logging.warning(f'Date parse failed: {e}')
    gl['Date'] = pd.NaT
```

### Recipe 7.2: Validation Checks

Code:

```python
def validate_inputs(df):
    checks = {
        'has_account': 'Account' in df.columns,
        'has_amount': 'Amount' in df.columns,
        'no_blanks': df.isnull().sum().sum() == 0,
        'amounts_numeric': df['Amount'].dtype in ['int64', 'float64']
    }
    
    failed = [k for k, v in checks.items() if not v]
    if failed:
        raise ValueError(f'Validation failed: {failed}')
    
    return True
```

### Deliverable

Updated script with try/except blocks, logging, and input validation. Runs without crashing on bad data.

---

## Week 8: End-to-End Testing & First Production Run

### Goal

Run the complete month-end automation with real data. Document the process. Build templates for next month. Celebrate.

### Time Allocation

- End-to-end test with real data: 1 hour
- Document script & instructions: 1 hour
- Create template & handoff docs: 1 hour

### What to Test

- Run script with actual month-end GL extract
- Spot-check a few entries against source GL in ERP
- Verify GL total matches monthly report
- Check that all cost centers appear in summary
- Run reconciliation check against subledger

### Deliverable

- Working Python script
- README with instructions
- Sample output for next month's reference
- Changelog log showing what ran and when

---

## Beyond Week 8: Next Steps

### Once You're Done

- Extend to other reports (AP aging, AR aging, inventory reconciliation)
- Add email notifications when script completes
- Schedule with Windows Task Scheduler to run automatically on the 1st of each month
- Add interactive parameters (choose month/year at runtime)
- Store historical results in a database rather than files

---

## Resources

- Pandas documentation: https://pandas.pydata.org/docs
- OpenPyXL for advanced Excel formatting: https://openpyxl.readthedocs.io/
- Python logging: https://docs.python.org/3/library/logging.html
- Stack Overflow for error messages (search exact error text)