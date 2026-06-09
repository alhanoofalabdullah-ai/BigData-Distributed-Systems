from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder \
    .appName("Revenue Summary") \
    .getOrCreate()

df = spark.read.csv("data/raw/sales-transactions.csv", header=True, inferSchema=True)

total_revenue = df.agg(
    sum("amount").alias("total_revenue")
)

total_revenue.show()

total_revenue.write.mode("overwrite").csv("data/output/revenue-summary")

spark.stop()
