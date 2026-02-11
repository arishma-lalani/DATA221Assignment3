# Question 5

import pandas as pd

# Set pandas setting so that large variable names are shown in the output
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Load the dataset "student.csv"
student_df = pd.read_csv("student.csv")

# Create the grade_band column and tell the program what is categorized as low, medium, and high
def create_grade_band_column(grade):
    if grade <= 9:
        return "Low"
    elif 10 <= grade <= 14:
        return "Medium"
    else:  # grade >= 15
        return "High"

# Create a column that is called "grade_band" and apply it to the "grade" column for each student under "student.csv"
student_df["grade_band"] = student_df["grade"].apply(create_grade_band_column)

# Group by grade_band
grouped_summary_table = student_df.groupby("grade_band").agg(
    # Count the number of students that are in each grade band
    number_of_students=("grade", "count"),
    # Calculate the average number of absences that are in each grade band
    average_absences=("absences", "mean"),
    # Calculate the percentage of students with internet access
    percentage_of_students_with_internet_access=("internet", lambda x: (x.sum() / len(x)) * 100)
).reset_index()

# Save the grouped summary table to the new csv file
grouped_summary_table.to_csv("student_bands.csv", index=False)

# Print the table
print(grouped_summary_table)