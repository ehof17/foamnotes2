
### Arrays
```python
from pyspark.sql.functions import array, struct, lit

df = df.withColumn("scores", array(lit(85), lit(90), lit(78)))

```
### Maps

```python
from pyspark.sql.types import StructField, StructType, StringType, MapType

schema = StructType([
    StructField('name', StringType(), True),
    StructField("properties", MapType(StringType(), StringType()), True)
])
```

