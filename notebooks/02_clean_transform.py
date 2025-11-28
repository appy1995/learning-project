from pyspark.sql.functions import col, to_date

df = spark.read.parquet("/Workspace/Repos/appytong@gmail.com/learning-project/data/raw/raw_parquet")

df_clean = (
    df
    .dropDuplicates()
    .withColumn("release_date", to_date(col("release_date")))
    .filter(col("danceability").isNotNull())
    .filter(col("energy").isNotNull())
)

df_clean.write.mode("overwrite").parquet("Workspace/Repos/appytong@gmail.com/learning-project/data/clean/clean")