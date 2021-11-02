"""
Author: Nguyễn Duy Tâm
Date: 26/11/2000
Problem:
4. Define a function named summation. This function expects two numbers, named
low and high, as arguments. The function computes and returns the sum of the
numbers between low and high, inclusive
Solution:
"""
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))
