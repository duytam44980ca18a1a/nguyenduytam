"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
    Write a program that takes the radius of a sphere (a floating-point number) as
input and then outputs the sphere’s diameter, circumference, surface area, and
volume.
Solution:

    ....
"""
import math

# request the input
radius = float(input("Enter the sphere's radius: "))

# compute the results
diameter = 2 * radius
circumference = radius * math.pi
surfaceArea = 4 * math.pi * radius * radius
volume = 4 / 3.0 * math.pi * radius * radius * radius

# Display the results
print("diameter      :", diameter)
print("circumference :", circumference)
print("surfaceArea   :", surfaceArea)
print("volume        :", volume)
