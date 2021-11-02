"""
Author: Nguyễn Duy Tâm
Date: 26/11/2000
Problem:
 Define a function named even. This function expects a number as an argument and
returns True if the number is divisible by 2, or it returns False otherwise. (Hint: A
number is evenly divisible by 2 if the remainder is 0.)
Solution:
"""
def div(num1,num2):
  n = 0
  while n > 0:
    if num1%n == 0 and num2%n==0:
        print(True)
        n+=1
    else:
        print(False)
        