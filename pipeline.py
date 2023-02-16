from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.classification import LogisticRegression

def build_pipeline(input_col, output_col, categorical_cols, numeric_cols):
    # StringIndexer to convert categorical columns to numerical indices
    indexers = [StringIndexer(inputCol=col, outputCol=col+"_index") for col in categorical_cols]

    # OneHotEncoder to convert the indexed categorical columns to binary vectors
    encoders = [OneHotEncoder(inputCol=col+"_index", outputCol=col+"_vec") for col in categorical_cols]

    # Combine the categorical and numeric columns into a single feature vector
    assembler = VectorAssembler(inputCols=[col+"_vec" for col in categorical_cols] + numeric_cols, outputCol="features")

    # Define the logistic regression model
    lr = LogisticRegression(featuresCol="features", labelCol=output_col)

    # Create the pipeline
    pipeline = Pipeline(stages=indexers + encoders + [assembler, lr])

    return pipeline
