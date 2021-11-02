"""
Author: Nguyen Duy Tam
Date:26/11/2000
Problem:
  1. Write the outputs of the following loops:
a. for count in range(5):
 print(count + 1, end = " ")
b. for count in range(1, 4):
 print(count, end = " ")
c. for count in range(1, 6, 2):
 print(count, end = " ")
d. for count in range(6, 1, –1):
 print(count, end = " ")
Solution:

"""

for count in range(1, 6):
    print("count:", count)

for count in range(1, 4):
    print("count:", count)

for count in range(1, 6, 2):
    print("count:", count)

for count in range(6, 1, -1):
    print("count:", count)
