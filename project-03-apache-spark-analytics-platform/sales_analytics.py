from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count

spark = SparkSession.builder \
    .appName("Sales Analytics") \
    .getOrCreate()

df = spark.read.csv("data/raw/sales-transactions.csv", header=True, inferSchema=True)

sales_by_region = df.groupBy("region").agg(
    sum("amount").alias("total_sales"),
    count("transaction_id").alias("transaction_count")
)

sales_by_region.show()

sales_by_region.write.mode("overwrite").csv("data/output/sales-by-region")

spark.stop()
