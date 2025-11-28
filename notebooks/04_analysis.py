df = spark.read.parquet("/Workspace/Repos/appytong@gmail.com/learning-project/data/features/features")

# Popularity distribution
df_feat.select("popularity").display()

# Top artists by avg popularity
df_feat.groupBy("artists").avg("popularity") \
    .orderBy("avg(popularity)", ascending=False).display()

# Correlation example
df_feat.stat.corr("danceability", "energy")