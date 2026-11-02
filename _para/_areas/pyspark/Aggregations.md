# Built in aggreations
- sum, count, avg, max, min

You can preprocess using dataframe operations before using sql 

- By making each step a new temporary view, we can easily roll back and catch errors before they happen


### Handling data types

- Numerical data stored as strigns may not agg correctly.
- Cast can convert data types before processing
- 

```python
# Example of type casting
data = [("HR", "3000"), ("IT", "4000"), ("Finance", "3500")]
columns = ["Department", "Salary"]
df = spark.createDataFrame(data, schema=columns)

# Convert Salary column to integer
df = df.withColumn("Salary", df["Salary"].cast("int"))

# Perform aggregation
df.groupBy("Department").sum("Salary").show()
```

### RDDs for aggregations
> Typically would prefer data frames for this
```python
rdd = df.rdd.map(lambda row: (row["Department"], row["Salary"]))

rdd_aggregated = rdd.reduceByKey(lambda x, y: x+y)


print(rdd_aggregated.collect())
```


##### Best practices
- Filter early (Before aggs)
- Enusre data is clean and correctly typed
- Avoid operations that use entire dataset: minimize groupbys
- Prefer DataFrames
- Use explain() to inspect execution plans
