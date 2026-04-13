# PDF-to-Excel Financial Statement Parser

This repository contains a high-precision automation tool designed to extract trade-level transaction data from complex, unstructured financial PDF reports (e.g., broker statements) and convert them into structured Excel datasets.

# 📌 Problem & Solution

Financial institutions often provide trade history in PDF formats that use borderless tables and inconsistent layouts. Standard OCR tools frequently fail to capture these accurately, leading to "column shifting" errors and requiring hours of manual data entry.

This automation bot:

Replaces manual data entry by using coordinate-based parsing via pdfplumber.

Implements a floating-point tolerance check to identify and fix misaligned columns (e.g., identifying when commission is mistaken for price).

Automatically normalizes transaction sides (BUY/SELL) and deduplicates records.

Provides a built-in "Validation Report" to track missing symbols or extraction failures in real-time.

# 🛠 Tech Stack
**Python:** Core engine for data orchestration.

**Pdfplumber:** Advanced text extraction and coordinate-based parsing.

**Pandas & Numpy:** For data cleaning, deduplication, and handling missing values (NaN).

**Regex (Regular Expressions):** To identify specific transaction patterns and filter out headers/footers.

**Openpyxl:** For generating professional Excel workbooks.

# ⚙️ Core Automation Workflow
**Ingestion:** Opens and reads multi-page financial PDF statements.

**Regex Filtering:** Scans lines to isolate transaction rows based on date patterns (MM/DD).

**Transformation:** Logic-based parsing of quantity, symbol, side (BUY/SELL), and transaction costs.

**Validation & Loading:** Performs a final data integrity check and exports the cleaned dataset to a structured Excel file.

# 📊 Example Output
Upon execution, the bot generates a Data Validation Report to ensure auditability:

```
========================================
📊 STAGE 5: DATA VALIDATION REPORT
----------------------------------------
✅ Total Transactions Processed : 11
♻️  Duplicate Rows Removed       : 1
⚠️  Missing Symbols (NaN)       : 1
❌ Failed Price Extractions     : 0
========================================

    date  side symbol  quantity  price  total_amount  commission
0   7/11   BUY    JNK       100  37.18      -3725.85       -7.95
1   7/11   BUY   SBRA       200  11.04      -2215.95       -7.95
2   7/11  SELL    JNK       200  36.88       7368.45       -7.95
3   7/11  SELL    JNK       500  36.88      18432.55       -7.95
4   7/11   BUY   SBRA        50  11.03       -559.65       -7.95
5   7/11   BUY   SBRA        50  11.03       -559.45       -7.95
6   7/11   BUY   SBRA       150  11.05      -1665.45       -7.95
7   7/12   BUY    JNK        50  37.30      -1872.90       -7.95
8   7/18   BUY    JNK        50  38.28      -1921.90       -7.95
9   7/23   BUY    NaN      5000 109.00      -5450.00         NaN
10  7/30   BUY  FMPXX      1000   1.00      -1007.95       -7.95
```

# 🚀 How to Run
1. Place your PDF file in the data/ directory.

2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the automation:
```
python pdf_to_excel_bot/src/pdf_to_excel_bot.py
```

