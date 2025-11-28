from pyspark.sql.functions import year, floor

df_clean = spark.read.parquet("/Workspace/Repos/appytong@gmail.com/learning-project/data/clean/clean")

df_feat = (
    df_clean
    .withColumn("release_year", year("release_date"))
    .withColumn("decade", (floor(col("release_year") / 10) * 10))
    .withColumn("energy_dance_ratio", col("energy") / col("danceability"))
)

df_feat.write.mode("overwrite").parquet("dbfs:/FileStore/data/features/features")