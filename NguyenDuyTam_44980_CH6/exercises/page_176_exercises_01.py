"""
Author:Nguyen Duy Tam
Date: 26/11/2000
Problem:
 Draw a structure chart for one of the solutions to the programming projects of Chapters 4 and 5.
 The program should include at least two function definitions other than the main function.
Solution:
def test_prime(n):
if (n==1):
return False
elif (n==2):
return True;
else:
for x in range(2,n):
if(n % x==0):
return False
return True

print(test_prime(5))
print(is_even_num([1, 2, 3, 4, 5, 6, 7,10...
    ....
"""