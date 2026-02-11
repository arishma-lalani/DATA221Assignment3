# Question 4

import pandas as pd

# Load the csv file
student_df = pd.read_csv("student.csv")

# Filter students with conditions provided
filtered_students = student_df[
    (student_df["studytime"] >= 3) &
    (student_df["internet"] == 1) &
    (student_df["absences"] <= 5)
]

# Save the filtered dataFframe to a new csv file called "high_engagement.csv"
filtered_students.to_csv("high_engagement.csv", index=False)

# Print the number of students saved in the new csv file
number_of_students = len(filtered_students)
print("Number of students saved:", number_of_students)

# Print the average grade of the students
if number_of_students > 0:
    average_grade_of_students = filtered_students["grade"].mean()
    print("Average grade:", average_grade_of_students)

