"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
The kinetic energy of a moving object is given by the formula KE 1 2/ mv 5 2 ( )
where m is the object’s mass and v is its velocity. Modify the program you created
in Project 5 so that it prints the object’s kinetic energy as well as its momentum

Solution:
    ....
"""

# request the input
mass = float(input("Enter the object's mass: "))
velocity = float(input("Enter the object's velocity: "))

# compute the results
momentum = mass * velocity
kineticEnergy = (mass * velocity ** 2) / 2

# Display the results
print("The object's momentum is", momentum)
print("The object's kineticEnergy is", kineticEnergy)
