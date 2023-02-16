# using the pipeline from the previous dataset
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Load your dataset as a DataFrame
df = spark.read.csv("path/to/my/data.csv", header=True, inferSchema=True)

# Define the input and output columns, and the categorical and numeric columns
input_col = "features"
output_col = "label"
categorical_cols = ["categoryA", "categoryB"]
numeric_cols = ["numeric1", "numeric4", "numeric7"]

# Build the pipeline
pipeline = build_pipeline(input_col, output_col, categorical_cols, numeric_cols)

# Fit and transform the dataset using the pipeline
model = pipeline.fit(df)
transformed_df = model.transform(df)
