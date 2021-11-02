"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
   An object’s momentum is its mass multiplied by its velocity. Write a program
that accepts an object’s mass (in kilograms) and velocity (in meters per second) as
inputs and then outputs its momentum
Solution:
    ....
"""

# request the input
mass = float(input("Enter the object's mass: "))
velocity = float(input("Enter the object's velocity: "))

# compute the results
momentum = mass * velocity

# Display the results
print("The object's momentum is", momentum)
