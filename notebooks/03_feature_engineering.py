from pyspark.sql.functions import year, floor

df_clean = spark.read.table("workspace.default.clean_table")

df_feat = (
    df_clean
    .withColumn("release_year", year("release_date"))
    .withColumn("decade", (floor(col("release_year") / 10) * 10))
    .withColumn("energy_dance_ratio", col("energy") / col("danceability"))
)

df_feat.write.saveAsTable("workspace.default.feature_table")