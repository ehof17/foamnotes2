### Joins in Pyspark

DF1.join(DF2, on="columm", how="join_type")

```python
df_joined = df1.join(df2, df1.Id == df2.Name, "inner")
```

If you need to combine dfs with the same schema, use [[Union]]

[Union]: Union.md "Union"
