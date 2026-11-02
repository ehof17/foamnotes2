
# Leverage scale
- speed and efficienciy are the goal

- methods like broadcast will load a smaller dataset across the cluster using all available compute

```python
joined_df = large_df.join(broadcast(small_df),on="key",how="inner")
joined_df.show()

```
### Execcution plans
- Whenever operations are run in a dataframe, spark creats logical plan then its broken down into phyusical plan

```python
df.filter(df.Age > 40).select("Name").explain()

```


### Caching and Persisting

- Caching: store data in memory, for faster access for smaller datasets
- Persisting: Storing data in different storage levels for larger datasets


#### Persisting

```python
from pyspark import StorageLevel
# Can use disk when memory is inneficiant
df.persist(StorageLevel.MEMORY_AND_DISK)
# If data doesnt fit in memeory, spark writes overflow to disk. so operations can still proceed withoud crashing due to resource constraints


result = df.groupBy("col3").agg({"column4":"sum"})
result.show()

# unpersist after use
df.unpersist()
```

#### Optimizing pyspark
- Small subsections: Map preferred over groupbys
- Broadcast joins: for small datasets to load the data on all the nodes and avoid shuffle
- Avoid repeated actions
