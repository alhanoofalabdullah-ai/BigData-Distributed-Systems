from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("IoT Telemetry Processing") \
    .getOrCreate()

print("Telemetry Processing Started")
