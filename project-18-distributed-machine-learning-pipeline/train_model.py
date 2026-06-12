from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassifier

spark = SparkSession.builder \
    .appName("Distributed ML Training") \
    .getOrCreate()

print("Training model...")

spark.stop()
