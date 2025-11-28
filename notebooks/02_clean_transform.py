from pyspark.sql.functions import col, to_date

df = spark.read.table("workspce.default.raw_table")

df_clean = (
    df
    .dropDuplicates()
    .withColumn("release_date", to_date(col("release_date")))
    .filter(col("danceability").isNotNull())
    .filter(col("energy").isNotNull())
)

df_clean.write.saveAsTable("workspace.default.clean_table")