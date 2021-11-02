"""
Author: Nguyen Duy Tam
Date: 26/11/2000
Problem:
    Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
like to buy LP record albums. The store rents new videos for $3.00 a night, and
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
can use to calculate the total charge for a customer’s video rentals. The program
should prompt the user for the number of each type of video and output the total
cost.
Solution:
Program: fivestar.py
calculate the total charge for a customer's video renls,
given the nuber of each type ò video

NEW video rental = $3.00
oldie rental = $2.00

    ....
"""
# initialize constants
NEW_RENTAL = 3.00
OLDIE_RENTAL = 2.00

# requaest the inputs
newOnes = int(input("Enter the nubmer of new video: "))
oldOnes = int(input("Entter the number of oldies: "))

# compute the results
tatolcost = NEW_RENTAL * newOnes + OLDIE_RENTAL * oldOnes

# Display the results
print("the total cost is $" + str(round(tatolcost, 2)))
