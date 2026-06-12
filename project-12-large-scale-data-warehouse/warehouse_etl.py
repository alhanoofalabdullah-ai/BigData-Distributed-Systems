import subprocess

steps = [

    "etl/extract.py",

    "etl/transform.py",

    "etl/load.py"

]

for step in steps:

    subprocess.run(["python", step])

print("Warehouse ETL Completed")
