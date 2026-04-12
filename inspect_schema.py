import duckdb
import pandas as pd

con = duckdb.connect(r"C:\Users\Owner\Desktop\Isha Healthcare project\warehouse\healthcare.duckdb")

tables = [
    "claims",
    "claims_transactions",
    "patients",
    "encounters",
    "payers",
    "providers",
    "organizations",
    "procedures",
    "conditions",
]

all_rows = []

for table in tables:
    df = con.execute(f"DESCRIBE {table}").df()
    df["table_name"] = table
    all_rows.append(df)

final_df = pd.concat(all_rows, ignore_index=True)
final_df.to_csv("table_schema_summary.csv", index=False)

con.close()
print("Saved schema to table_schema_summary.csv")