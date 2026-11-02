# Handling missing data

Na.drop() to remove rows with null values


```python
# Drop rows with any nulls
df_cleaned = df.na.drop()

# filter out nulls
df_cleaned = df.where(col("columnName").isMotNull())

```

Or replace with a specific value

```
# Fill nulls in the age column with the value 0
df_filterd = df.na.fill({"age":0})
```
