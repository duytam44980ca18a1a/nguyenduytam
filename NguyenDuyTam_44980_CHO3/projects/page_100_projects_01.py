"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
    Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral
triangle.
Solution:
    ....
"""
AB = int(input("nhập độ dài cạnh AB: "))
BC = int(input("nhập độ dài cạnh BC: "))
CA = int(input("nhập độ dài cạnh CA: "))
if AB == BC == CA:
    print(" tam giác ABC là tam giác đều")
else:
    print(" tam giác ABC không phải là tam giác dều")
