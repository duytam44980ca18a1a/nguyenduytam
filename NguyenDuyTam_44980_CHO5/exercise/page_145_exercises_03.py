"""
Author: Nguyễn Duy Tâm
Date: 26/11/2000
Problem:
 What is a mutator method? Explain why mutator methods usually return the
value None
Solution:
The Mutator method is used to modify the variable values. This method does not require returning any value.
So, the return value of this method is none.
2.
def  listsum(numList):
     theSum = 0
     for i in numList:
         theSum = theSum + i
     return theSum
"""