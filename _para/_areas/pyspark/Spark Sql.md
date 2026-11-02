# Spark sql
- Module in Apache Spark for structured data processing
- Allows us to run SQL queries alongside data processing tasks
- Seamless combination of Python and SQL in one application

Register a dataframe as a temporary view

```python
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("Spark SQL Example").getOrCreate()

# Sample DataFrame
data = [("Alice", "HR", 30), ("Bob", "IT", 40), ("Cathy", "HR", 28)]
columns = ["Name", "Department", "Age"]
df = spark.createDataFrame(data, schema=columns)

# Register DataFrame as a temporary view
df.createOrReplaceTempView("people")

# Query using SQL
result = spark.sql("SELECT Name, Age FROM people WHERE Age > 30")
result.show()


```



