# Question 6

import pandas as pd

# Load the "crime.csv" dataset into a DataFrame
crime_df = pd.read_csv("crime.csv")

# Create a new column called the risk column based on ViolentCrimesPerPop
def assign_crime_risk_rate(violent_crime_rate):
    if violent_crime_rate >= 0.50:
        return "HighCrime"
    else:
        return "LowCrime"

crime_df["risk"] = crime_df["ViolentCrimesPerPop"].apply(assign_crime_risk_rate)

# Group the data by risk and calculate the average unemployment rate
average_unemployment_by_risk = crime_df.groupby("risk")["PctUnemployed"].mean()

# Print the average unemployment rate for both HighCrime and LowCrime groups
print(f"HighCrime Unemployment Rate: {average_unemployment_by_risk['HighCrime']}")
print(f"LowCrime Unemployment Rate: {average_unemployment_by_risk['LowCrime']}")
