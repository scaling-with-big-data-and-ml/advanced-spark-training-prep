from pyspark.sql import SparkSession


# Simple application to play with Spark. If the code below works, you're good to go for the course!
if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("Playground").getOrCreate()
    df = spark.read.json("../data/cars")
    df.show()
