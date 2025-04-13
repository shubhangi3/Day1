from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("SalesDataAnalysis").getOrCreate()

# Read CSV from local Windows path (using file:/// prefix)
df = spark.read.csv("file:///C:/Users/Acer/PycharmProjects/pythonProject5/input_data/orders1_gb.csv", header=True, inferSchema=True)

# Show data
df.show()


