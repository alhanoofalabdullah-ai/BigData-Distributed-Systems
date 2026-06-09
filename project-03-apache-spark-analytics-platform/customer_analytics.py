from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count

spark = SparkSession.builder \
    .appName("Customer Analytics") \
    .getOrCreate()

df = spark.read.csv("data/raw/sales-transactions.csv", header=True, inferSchema=True)

customer_summary = df.groupBy("customer_id").agg(
    sum("amount").alias("total_spent"),
    count("transaction_id").alias("total_transactions")
)

customer_summary.show()

customer_summary.write.mode("overwrite").csv("data/output/customer-summary")

spark.stop()
