"""
Author:Nguyen Duy Tam
Date: 26/11/2000
Problem:
    You can calculate the surface area of a cube if you know the length of an edge.
Write a program that takes the length of an edge (an integer) as input and prints
the cube’s surface area as output.
Solution:
Program: cube.py
Compute the surfacea area of the cube.
the input is the cube's edge
the ouput í the surface area of the cube

    ....
"""

# Request the inputs
edge = float(input("enter the cube's edge"))

# Compute the surface ares
surfacearea = edge * edge * 6

# Display the income tax
print("then susface ares is", surfacearea, "square units")
