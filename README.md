# pyspark_pipeline
A pipeline built using PySpark.

This is a simple ML pipeline built using PySpark that can be used to perform logistic regression on a given dataset.
This function takes four arguments: 
####### input_col (the name of the input column in your dataset), 
####### output_col (the name of the output column you want to predict), 
####### categorical_cols (a list of the names of the categorical columns in your dataset), 
####### and numeric_cols (a list of the names of the numeric columns in your dataset).

It then creates a 'pipeline' with 4 stages:

StringIndexer: Each categorical column is converted to a numerical index.
OneHotEncoder: Each numerical index is converted to a binary vector.
VectorAssembler: The binary vectors and numeric columns are combined into a single feature vector.
LogisticRegression: The logistic regression model is trained on the feature vectors and output column.

The function returns the 'pipeline' (better names have been used before), which can be used to fit and transform the dataset as shown in the transformer.py file.
