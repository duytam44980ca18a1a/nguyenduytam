"""
Author: Nguyễn Duy Tâm
Date: 26/11/2000
Problem:
Write a loop that replaces each number in a list named data with its absolute value
Solution:
"""
# Some positive and negative values
values = [-40, 58, -69, -84, 51, 76, -12, 36]

# Take the absolute value of negative values, but
# multiply positive values with 2
processed = []
for number in values:
    if number < 0:
        processed.append(abs(number))
    else:
        processed.append(number * 2)

# Output data
print("Original numbers:\n", values)
print("Processed numbers:\n", processed)