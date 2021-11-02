"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
    Translate the following for loops to equivalent while loops:
a. for count in range(100):
 print(count)
b. for count in range(1, 101):
 print(count)
c. for count in range(100, 0, –1):
 print(count)
Solution:
a.
count = 0
while count < 100:
 print(count)
 count += 1
 b.
 count = 100
while count > 0:
 print(count)
 count -= 1
 c.
 count = 10
while count >= 1:
 print(count, end = " ")
 count -= 1
    ....
"""