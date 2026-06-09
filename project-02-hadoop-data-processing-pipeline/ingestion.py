import shutil
import os

source = "sample-data/sales-data.csv"

destination = "hdfs/input/sales-data.csv"

os.makedirs("hdfs/input", exist_ok=True)

shutil.copy(source, destination)

print("Data ingestion completed")
