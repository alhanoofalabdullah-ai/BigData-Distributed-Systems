from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder \
    .appName("Product Analytics") \
    .getOrCreate()

df = spark.read.csv("data/raw/sales-transactions.csv", header=True, inferSchema=True)

product_summary = df.groupBy("product").agg(
    sum("amount").alias("product_revenue"),
    sum("quantity").alias("quantity_sold")
)

product_summary.show()

product_summary.write.mode("overwrite").csv("data/output/product-summary")

spark.stop()
