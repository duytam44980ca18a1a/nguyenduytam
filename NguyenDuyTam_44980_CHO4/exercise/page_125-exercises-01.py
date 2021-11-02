"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
Write a code segment that opens a file named myfile.txt for input and prints the
number of lines in the file.
Solution:

"""
f = open("myfile.txt", 'r')
for line in f:
    print(line)
