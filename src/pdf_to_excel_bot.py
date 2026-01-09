import pdfplumber
import re
import pandas as pd
import numpy as np

# --- CONFIG ---
PDF_PATH = "data/brokerstatement.pdf"
DATE_PATTERN = r"^([1-9]|1[0-2])/([0-9]{1,2})"  # Lines starting with date (MM/DD)

def extract_trades(pdf_path):
    all_trades = []

    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[10]  # Page containing trade table
        content = page.extract_text()

    lines = content.split("\n")
    trade_lines = [line for line in lines if re.match(DATE_PATTERN, line)]

    for line in trade_lines:
        parts = line.split()
        trade = {}

        trade["date"] = parts[0]

        # Transaction side
        if "bought" in parts:
            trade["side"] = "BUY"
        elif "sold" in parts:
            trade["side"] = "SELL"
        else:
            trade["side"] = "UNKNOWN"

        # Symbol detection
        if "You" in parts:
            you_idx = parts.index("You")
            ticker_candidate = parts[you_idx - 1]
            if ticker_candidate.isupper() and ticker_candidate.isalpha() and 2 <= len(ticker_candidate) <= 5:
                trade["symbol"] = ticker_candidate
            else:
                trade["symbol"] = np.nan
        else:
            trade["symbol"] = np.nan

        # Quantity and Price
        quantity = None
        price = None
        for i, p in enumerate(parts):
            if p.replace("-", "").replace(",", "").replace(".", "").isdigit():
                val = int(p.replace(",", ""))
                quantity = -val if trade["side"] == "SELL" else val
                if i + 1 < len(parts):
                    try:
                        price = float(parts[i + 1].replace("$", "").replace(",", ""))
                    except ValueError:
                        price = None
                break
        trade["quantity"] = quantity
        trade["price"] = price

        # Total and Commission
        try:
            trade["total_amount"] = float(parts[-1].replace("$", "").replace(",", ""))
        except (ValueError, IndexError):
            trade["total_amount"] = None

        try:
            last_second_val = float(parts[-2].replace("$", "").replace(",", ""))
            if price is not None and abs(last_second_val - price) < 0.0001:
                trade["commission"] = np.nan
            else:
                trade["commission"] = last_second_val
        except (ValueError, IndexError):
            trade["commission"] = np.nan

        all_trades.append(trade)

    return pd.DataFrame(all_trades)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    df_raw = extract_trades(PDF_PATH)

    # Clean data: remove duplicates and check missing values
    initial_count = len(df_raw)
    df_clean = df_raw.drop_duplicates().reset_index(drop=True)
    final_count = len(df_clean)

    missing_symbols = df_clean['symbol'].isnull().sum()
    missing_prices = df_clean['price'].isnull().sum()

    print("\n" + "="*40)
    print("📊 DATA VALIDATION REPORT")
    print("-" * 40)
    print(f"✅ Total Transactions Processed : {final_count}")
    print(f"♻️  Duplicate Rows Removed       : {initial_count - final_count}")
    print(f"⚠️  Missing Symbols (NaN)       : {missing_symbols}")
    print(f"❌ Failed Price Extractions     : {missing_prices}")
    print("="*40 + "\n")

    pd.set_option('display.max_rows', None)
    pd.set_option('display.float_format', '{:.2f}'.format)

    print(df_clean)

    df_clean.to_excel("data/Trade_Statement_Analysis.xlsx", index=False)
