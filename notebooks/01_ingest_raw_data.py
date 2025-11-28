raw_df = spark.read.csv("/Workspace/Repos/appytong@gmail.com/learning-project/data/raw/dataset.csv", header=True, inferSchema=True)

raw_df.printSchema()
raw_df.limit(5).display()
raw_df.count()

raw_df.write.mode("overwrite").parquet("/Workspace/Repos/appytong@gmail.com/learning-project/data/raw/raw_parquet")