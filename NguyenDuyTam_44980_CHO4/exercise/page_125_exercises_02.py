"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
Write a code segment that opens a file for input and prints the number of
four-letter words in the file
Solution:

"""
f = open("myfile.txt", 'r')
while True:
    line = f.readline()
    if line == "":
        break
    print(line)

