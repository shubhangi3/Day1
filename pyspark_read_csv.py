from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("SalesDataAnalysis").getOrCreate()

# Load CSV into PySpark DataFrame
df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

# Show first few rows
df.show()
