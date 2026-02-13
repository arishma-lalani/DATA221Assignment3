import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the csv file: "kidney_disease.csv"
kidney_disease_dataframe = pd.read_csv("kidney_disease.csv")

# Create a feature matrix X that contains all columns except the 'classification' column
kidney_disease_feature_matrix_all_columns_except_classification = kidney_disease_dataframe.drop(
    columns=['classification'])

# Create a label vector y using the 'classification' column
kidney_disease_target_label_vector_classification_column = kidney_disease_dataframe['classification']

# Change the string columns into numeric values
kidney_disease_categorical_columns = kidney_disease_feature_matrix_all_columns_except_classification.select_dtypes(
    include=['object']).columns
kidney_disease_feature_matrix_encoded_for_knn = kidney_disease_feature_matrix_all_columns_except_classification.copy()

# Change everything to a string first so that it can handle the missing values
for column in kidney_disease_categorical_columns:
    label_encoder_for_column = LabelEncoder()
    kidney_disease_feature_matrix_encoded_for_knn[column] = kidney_disease_feature_matrix_encoded_for_knn[column].astype(str)
    kidney_disease_feature_matrix_encoded_for_knn[column] = label_encoder_for_column.fit_transform(
        kidney_disease_feature_matrix_encoded_for_knn[column])

# Replace missing values with the average value of that column
kidney_disease_imputer_mean_strategy = SimpleImputer(strategy='mean')
kidney_disease_feature_matrix_imputed_for_knn = kidney_disease_imputer_mean_strategy.fit_transform(
    kidney_disease_feature_matrix_encoded_for_knn)

# Split the dataset into training and testing sets
# # Training data = 70%, Testing data = 30%, random_state ensures that it can be reproduced
kidney_disease_feature_matrix_training_set, kidney_disease_feature_matrix_testing_set, \
    kidney_disease_target_label_vector_training_set, kidney_disease_target_label_vector_testing_set = train_test_split(
    kidney_disease_feature_matrix_imputed_for_knn,
    kidney_disease_target_label_vector_classification_column,
    test_size=0.3,
    random_state=42
)

# Train the K-nearest neighbors classifier (k = 1, 3, 5, 7, 9)
k_values_for_knn_experiment = [1, 3, 5, 7, 9]
kidney_disease_knn_test_accuracy_results = {}

for k_neighbors_value in k_values_for_knn_experiment:
    kidney_disease_knn_classifier = KNeighborsClassifier(n_neighbors=k_neighbors_value)
    kidney_disease_knn_classifier.fit(
        kidney_disease_feature_matrix_training_set,
        kidney_disease_target_label_vector_training_set
    )

    # Make predictions on test set
    kidney_disease_knn_predictions_test_set = kidney_disease_knn_classifier.predict(
        kidney_disease_feature_matrix_testing_set)

    # Compute the accuracy
    kidney_disease_knn_test_accuracy = accuracy_score(
        kidney_disease_target_label_vector_testing_set,
        kidney_disease_knn_predictions_test_set
    )
    kidney_disease_knn_test_accuracy_results[k_neighbors_value] = kidney_disease_knn_test_accuracy

# Create a table to put the results in and print it
kidney_disease_knn_accuracy_table = pd.DataFrame(
    list(kidney_disease_knn_test_accuracy_results.items()),
    columns=['k_neighbors', 'Test_Accuracy']
)
print("KNN Test Accuracy for different k values (Kidney Disease Dataset):")
print(kidney_disease_knn_accuracy_table)

# Find the k with highest accuracy and print it
best_k_for_kidney_disease_knn = max(kidney_disease_knn_test_accuracy_results,
                                    key=kidney_disease_knn_test_accuracy_results.get)
print(f"\nThe value of k with highest test accuracy is: {best_k_for_kidney_disease_knn} with accuracy {kidney_disease_knn_test_accuracy_results[best_k_for_kidney_disease_knn]}")

# The k-value tells the model how many neighbors it should consider when
# coming to a conclusion. Very small values of k causes overfitting because
# the model memorizes a singular data point, which in turn means that the model
# hasn't learned accurately and has just memorized. A very large k-value
# results in underfitting because it neglects patterns that is crucial to
# learn the data accurately. Finding the right k-value depending on the model
# guarantees that the model is accurate.