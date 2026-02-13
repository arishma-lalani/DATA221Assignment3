import pandas as pd
from sklearn.model_selection import train_test_split

# Load the csv file: "kidney disease.csv"
kidney_disease_dataframe = pd.read_csv("kidney_disease.csv")

# Create a feature matrix X that contains all columns except the 'classification' column
kidney_disease_feature_matrix_all_columns_except_classification = kidney_disease_dataframe.drop(columns=['classification'])

# Create a label vector y using the 'classification' column
kidney_disease_target_label_vector_classification_column = kidney_disease_dataframe['classification']

# Split the dataset into training and testing sets
# Training data = 70%, Testing data = 30%, random_state ensures that it can be reproduced
kidney_disease_feature_matrix_training_set, kidney_disease_feature_matrix_testing_set, \
kidney_disease_target_label_vector_training_set, kidney_disease_target_label_vector_testing_set = train_test_split(
    kidney_disease_feature_matrix_all_columns_except_classification,
    kidney_disease_target_label_vector_classification_column,
    test_size = 0.3,
    random_state = 42
)

# Why we should not train and test a model on the same data? What is the purpose of the testing set?

# We should not train and test a model on the same data because the training
# data is what the model learns from and the testing data is the data we use
# to see if it actually learned. If you train and test on the same dataset,
# it will solely memorize instead of learning the patterns of the data. When
# a model memorizes the training data, this is called overfitting. The
# model focuses on one dataset and is not fitting for various datasets.
# Overfitting disregards the whole purpose of a testing set, which is to
# make generalizations so that it can be applying to new data.
