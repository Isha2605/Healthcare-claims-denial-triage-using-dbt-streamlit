from pathlib import Path
import duckdb

# Project root = folder where this script lives
project_root = Path(__file__).resolve().parent

# DuckDB database path
db_path = project_root / "warehouse" / "healthcare.duckdb"

print("Using DB:", db_path)

# Connect to DuckDB
con = duckdb.connect(str(db_path))

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

for table in tables:
    print(f"\n===== {table.upper()} =====")
    result = con.execute(f"DESCRIBE {table}").fetchall()
    for row in result:
        print(row)

con.close()