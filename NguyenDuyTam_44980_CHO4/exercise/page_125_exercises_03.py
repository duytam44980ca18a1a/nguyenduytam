"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
Assume that a file contains integers separated by newlines. Write a code segment
that opens the file and prints the average value of the integers.
Solution:

"""
f = open("integers.txt", 'r')
theSum = 0
for line in f:
    line = line.strip()
    number = int(line)
    theSum += number
print("The sum is", theSum)
