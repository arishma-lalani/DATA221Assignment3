import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


# Load the csv file: "kidney_disease.csv"
kidney_disease_dataframe = pd.read_csv("kidney_disease.csv")

# Create a feature matrix X that contains all columns except the 'classification' column
kidney_disease_feature_matrix_all_columns_except_classification = kidney_disease_dataframe.drop(
    columns=["classification"]
)

# Create a label vector y using the 'classification' column
kidney_disease_target_label_vector_classification_column = kidney_disease_dataframe["classification"]


# Change the string columns into numeric values
kidney_disease_feature_matrix_all_columns_except_classification = pd.get_dummies(
    kidney_disease_feature_matrix_all_columns_except_classification,
    drop_first=True
)

# Replace missing values with the average value of that column
kidney_disease_feature_matrix_all_columns_except_classification = (
    kidney_disease_feature_matrix_all_columns_except_classification.fillna(
        kidney_disease_feature_matrix_all_columns_except_classification.mean()
    )
)

# Split the dataset into training and testing sets
# Training data = 70%, Testing data = 30%, random_state ensures that it can be reproduced
kidney_disease_feature_matrix_training_set, kidney_disease_feature_matrix_testing_set, \
kidney_disease_target_label_vector_training_set, kidney_disease_target_label_vector_testing_set = train_test_split(
    kidney_disease_feature_matrix_all_columns_except_classification,
    kidney_disease_target_label_vector_classification_column,
    test_size=0.30,
    random_state=42
)


# Train the K-nearest neighbors classifier (k = 5)
k_nearest_neighbors_classifier_k_equals_5 = KNeighborsClassifier(n_neighbors=5)

k_nearest_neighbors_classifier_k_equals_5.fit(
    kidney_disease_feature_matrix_training_set,
    kidney_disease_target_label_vector_training_set
)

# Conduct predictions on the data
kidney_disease_predicted_labels_testing_set = (
    k_nearest_neighbors_classifier_k_equals_5.predict(
        kidney_disease_feature_matrix_testing_set
    )
)

# Compute the matrix
kidney_disease_confusion_matrix = confusion_matrix(
    kidney_disease_target_label_vector_testing_set,
    kidney_disease_predicted_labels_testing_set
)

# Compute the accuracy
kidney_disease_accuracy = accuracy_score(
    kidney_disease_target_label_vector_testing_set,
    kidney_disease_predicted_labels_testing_set
)

# Compute the precision
kidney_disease_precision = precision_score(
    kidney_disease_target_label_vector_testing_set,
    kidney_disease_predicted_labels_testing_set,
    pos_label="ckd"
)

# Compute the recall
kidney_disease_recall = recall_score(
    kidney_disease_target_label_vector_testing_set,
    kidney_disease_predicted_labels_testing_set,
    pos_label="ckd"
)

# Compute the F1-score
kidney_disease_f1_score = f1_score(
    kidney_disease_target_label_vector_testing_set,
    kidney_disease_predicted_labels_testing_set,
    pos_label="ckd"
)

# Print all the results
print("Confusion Matrix:\n", kidney_disease_confusion_matrix)
print("Accuracy:", kidney_disease_accuracy)
print("Precision:", kidney_disease_precision)
print("Recall:", kidney_disease_recall)
print("F1-score:", kidney_disease_f1_score)

# In this case, the true positive is correctly identifying a person who
# has the kidney disease, whereas the true negative is accurately identifying
# a person who does not have the disease. On the other hand, the false
# positive is falsely ruling out that a person has kidney disease when they
# do not. The false negative is ruling out the patient health when they do
# in fact have the kidney disease.

# Just accuracy may not be enough to evaluate a classification model because
# it may guess a certain outcome for different populations sizes. This is
# called an accuracy paradox, and occurs when the model looks accurate but
# fails to rule out a person with kidney disease. In medical settings, it
# crucial to ensure no patient receives a false diagnosis, which is why the
# recall is the most important metric. This is because it computes the
# percentage of truly sick people and compare it to the model to see if it
# got it right, and so that it detects as many possible sick patients as it
# can.