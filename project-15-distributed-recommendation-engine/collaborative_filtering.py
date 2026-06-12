from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS

spark = SparkSession.builder \
    .appName("Collaborative Filtering") \
    .getOrCreate()

ratings = spark.read.csv(
    "datasets/ratings.csv",
    header=True,
    inferSchema=True
)

als = ALS(
    maxIter=5,
    regParam=0.01,
    userCol="customer_id",
    itemCol="product_id",
    ratingCol="rating"
)

model = als.fit(ratings)

recommendations = model.recommendForAllUsers(5)

recommendations.show()

spark.stop()
