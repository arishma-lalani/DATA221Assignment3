import pandas as pd

# Load the csv file: "crime.csv"
crime_dataset_dataframe = pd.read_csv("crime.csv")

# Tell the program to focus on the ViolentCrimesPerPop column
violent_crimes_per_population_series = crime_dataset_dataframe["ViolentCrimesPerPop"]

# Compute the mean, median, standard deviation, minimum value and maximum value for this column
violent_crimes_per_population_mean = violent_crimes_per_population_series.mean()
violent_crimes_per_population_median = violent_crimes_per_population_series.median()
violent_crimes_per_population_standard_deviation = violent_crimes_per_population_series.std()
violent_crimes_per_population_minimum = violent_crimes_per_population_series.min()
violent_crimes_per_population_maximum = violent_crimes_per_population_series.max()

# Print the statistics from above
print("Mean:", violent_crimes_per_population_mean)
print("Median:", violent_crimes_per_population_median)
print("Standard Deviation:", violent_crimes_per_population_standard_deviation)
print("Minimum:", violent_crimes_per_population_minimum)
print("Maximum:", violent_crimes_per_population_maximum)


# Compare the mean and median. Does the distribution look symmetric or skewed? Explain briefly.
# Since the mean is greater than the median, the distribution
# of violent crimes per population looks right-skewed. This means that
# there are some communities with very high crime rates that shift the
# mean up. We can also tell from the maximum value being way larger than
# the minimum value. This tells us that there is a long tail on the
# right side, which is essentially what it means to be right-skewed.
# If the mean and median are close to each other, we can conclude that
# the distribution would look almost symmetric.

# If there are extreme values (very large or very small), which statistic is more affected: mean or median? Explain why.
# The mean is more affected by extreme values because the mean. This is
# because when calculating the mean, we take the sum of all the values
# and divide it by the number of values there are. This also accounts
# for any outliers that are present. This is why extreme values contribute
# to the mean greatly. The median however, only shifts a little because
# when extreme values are added, they are added either to the beginning
# or end of a list, usually keeping the middle value about the same.