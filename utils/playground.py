from pyspark.sql import SparkSession


if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("Playground").getOrCreate()
    df = spark.read.json("../data/cars")
    df.show()
