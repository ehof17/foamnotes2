# User Defined Functions (UDF)
- Custom function we create to work with data using pyspark dataframe

Advantages
- Reuse and repeat common tasks
- Registered directly with spark and can be shared
- Pyspark DataFrames (for smalled datasets)
- pandas UDFs (for larger datasets)


### Defining and registering a UDF

```python
def to_uppercase(s):
    return s.upper() if s else None

# register
to_uppercase_udf = udf(to_uppercase, StringType())

# Apply the UDF
df = df.withColumn("name_upper", to_uppercase_udf(df["name"]))

df.show()

```

- Can introduce performance overhead
- Because pyspark has to do a ton of conversions
- To mitigate this, pyspark introduced pandas udf


```python
from pyspark.sql.functions import pandas_udf

@pandas_udf("float")
def fahrenheit_to_celsius_pandas(temp_f):
    return (temp_f - 32) * 5.0/9.0


```



#### Pyspark UDF
- Relatively small data sets
- Simple transformations like data cleaning
- Changes occur at the columnar level, not row level
- Must be registered o spark session with udf


#### pandas udf
- relatively large datasets
- Complex operations beyond simple data cleaning
- Specific row level changes over column level
- Can be called outside spark session
