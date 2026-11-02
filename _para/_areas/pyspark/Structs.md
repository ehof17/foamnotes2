# Structs
- Manage heirarchal data in one column

```python
df = df.withColumn("name_struct", struct("first_name", "last_name"))


```
