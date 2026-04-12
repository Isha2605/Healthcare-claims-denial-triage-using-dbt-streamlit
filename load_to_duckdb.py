from pathlib import Path
import pandas as pd
import duckdb

# Project paths
project_root = Path(r"C:\Users\Owner\Desktop\Isha Healthcare project")
raw_dir = project_root / "data" / "raw" / "synthea_csv"
db_path = project_root / "warehouse" / "healthcare.duckdb"

print("Project root:", project_root)
print("Raw dir:", raw_dir)
print("Raw dir exists:", raw_dir.exists())
print("DB path:", db_path)

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
    file_path = raw_dir / f"{table}.csv"
    print(f"Checking {file_path} ...")

    if not file_path.exists():
        print(f"Could not find file for table: {table}")
        continue

    print(f"Loading {table} ...")
    df = pd.read_csv(file_path)
    con.register("temp_df", df)
    con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM temp_df")
    con.unregister("temp_df")

print("\nLoaded tables successfully.\n")

for table in tables:
    try:
        count = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"{table}: {count} rows")
    except Exception as e:
        print(f"{table}: not loaded ({e})")

con.close()