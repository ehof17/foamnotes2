# Resilient Distributed Dataset
Distrubuted data collections across a cluster with automatic recovery from node failurs

- Good for large scale data
- Immutable, but a new RDD can be created using functions like map or filter

### Creating an RDD

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("RDDExample").getOrCreate()

census_df = spark.read.csv("/census.csv")
# Conversion
census_rdd = census_df.rdd

census_rdd.collect()
```

### Showing Collect
``` python
data_collected = df.collect()
for row in data_collected:
    print(row)
```


### Useful functions and methods

- Map: method applies functions across dataset:
  - rdd.map(map_function)
- Collect: Collects data from across the cluster
  - rdd.collect()
- 
