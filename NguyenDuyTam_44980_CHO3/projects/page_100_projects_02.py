"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
    Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle.
Recall from the Pythagorean theorem that in a right triangle, the square of
one side equals the sum of the squares of the other two sides.
Solution:
    ....
"""
AB = int(input("nhập độ dài cạnh AB: "))
BC = int(input("nhập độ dài cạnh BC: "))
CA = int(input("nhập độ dài cạnh CA: "))
if AB**2 == BC**2 + CA**2:
    print("tam giác ABC  là tam giác vuông")
elif BC**2 == CA**2 + AB**2:
    print("tam giác ABC  là tam giác vuông")
elif CA ** 2 == BC ** 2 + AB ** 2:
    print("tam giác ABC  là tam giác vuông")
else:
    print("tam giác ABC không phải là tam giác vuông")
