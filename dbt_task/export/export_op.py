from google.cloud import bigquery
import pandas as pd
import os

# ---------- CONFIG ----------
PROJECT_ID = "cl-project-482713"     # your GCP project
DATASET = "dbt_task"                 # dbt schema
OUTPUT_DIR = "../data"

TABLES = {
    "first_click": "first_click_op.csv",
    "last_click": "last_click_op.csv"
}
# ----------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

client = bigquery.Client(project=PROJECT_ID)

for table, file_name in TABLES.items():
    query = f"""
        SELECT *
        FROM `{PROJECT_ID}.{DATASET}.{table}`
    """
    print(f"Exporting {table}...")

    df = client.query(query).to_dataframe()
    output_path = os.path.join(OUTPUT_DIR, file_name)
    df.to_csv(output_path, index=False)

    print(f"Saved to {output_path}")

print("✅ Export completed")
