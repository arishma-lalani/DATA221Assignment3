import pandas as pd
import matplotlib.pyplot as plt

# Load the csv file: "crime.csv"
crime_dataset_dataframe = pd.read_csv("crime.csv")

# Tell the program to focus on the ViolentCrimesPerPop column
violent_crimes_per_population_series = crime_dataset_dataframe["ViolentCrimesPerPop"]

# Create the histogram to show how all the values are distributed
plt.figure()
plt.hist(violent_crimes_per_population_series, bins=20, edgecolor='black')
plt.title("Histogram of the Distribution of Violent Crimes Per Population")  # Title of Histogram
plt.xlabel("Violent Crimes Per Population")  # x-axis label
plt.ylabel("Frequency")  # y-axis label
plt.show()  # Show the histogram

# # Create the boxplot to show how all the values are distributed
plt.figure()
plt.boxplot(violent_crimes_per_population_series)
plt.title("Box Plot of the Distribution of Violent Crimes Per Population")  # Title of Boxplot
plt.xlabel("Violent Crimes Per Population")  # x-axis label
plt.ylabel("Value")  # y-axis label
plt.show()


# The histogram shows that most communities have low to medium rates of
# violent crimes, with a very small number of communities that very
# extremely high values. The data is more concentrated toward the
# lower part of the histogram. We can also visually see the right-skewed
# nature of the graph. This tells us that high crime rates are
# uncommon but very extreme when they do show up.

# The box plot shows the median closer to the 25th percentile, which
# means that the data is right-skewed. The box plot does not showcase
# any points beyond the handles, suggesting that all the points fall within
# the boxplot. This means that there are no outliers present.

