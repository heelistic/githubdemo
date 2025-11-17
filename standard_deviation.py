# GLAB 330.2.2 - Standard Deviation
# This script calculates the standard deviation for the given dataset:
# 2, 4, 4, 4, 5, 5, 7, 9

import math

data = [2, 4, 4, 4, 5, 5, 7, 9]

mean = sum(data) / len(data)

squared_differences = [(x - mean) ** 2 for x in data]

variance = sum(squared_differences) / len(squared_differences)

standard_deviation = math.sqrt(variance)

print("Dataset:", data)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
