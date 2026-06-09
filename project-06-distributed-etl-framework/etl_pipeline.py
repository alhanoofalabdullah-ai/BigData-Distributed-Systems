import subprocess

steps = [

    "transformation/clean_data.py",

    "transformation/validate_data.py",

    "transformation/normalize_data.py",

    "transformation/enrich_data.py",

    "loading/load_to_warehouse.py"

]

for step in steps:

    subprocess.run(["python", step])

print("ETL Pipeline Completed Successfully")
