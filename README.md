
# Automated PDF Trade Report Extraction and Excel Conversion

## Project Objective

This project automates the extraction of trade-level and transaction data from financial PDF reports (such as broker statements and trade summaries) and converts them into clean, structured Excel files suitable for analysis and reporting. The pipeline is specifically designed to handle unstructured data, borderless tables, and column shifting issues common in financial documents, ensuring high data integrity for audit and reconciliation purposes.

## Technologies Used

**Python:** Core programming language used for the extraction engine and automation.

**Pdfplumber:** For deep-level text extraction and coordinate-based parsing of PDF content.

**Pandas:** For data structuring, deduplication, and numerical analysis.

**Regex (Regular Expressions):** To identify transaction rows and filter out headers/footers.

**Numpy:** For handling missing values (NaN) and maintaining data type consistency.

**Openpyxl:** Engine for generating professional Excel workbooks.

## How to Run

1.	Ensure the required Python libraries are installed:

pip install -r requirements.txt

2.	Run the script:

python pdf_to_excel_bot.py

3.	After execution, check the terminal for the Data Validation Report and verify the generated Trade_Statement_Analysis.xlsx file.

## Why This Is Valuable for a Hedge Fund

-	Operational Efficiency: Eliminates manual data entry, reducing human error and saving significant back-office resources.
-	Advanced Data Integrity: Uses a floating-point tolerance check (< 0.0001) to detect and fix column shifting issues that standard OCR tools miss.
-	Audit-Ready Reporting: Provides a clean, deduplicated, and normalized (BUY/SELL sides) trade log essential for risk management.
-	Scalability: The regex-driven logic allows processing of multi-page statements without structural breakdown.
