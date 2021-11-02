"""
Author:Nguyễn Duy Tâm
Date: 26/11/2000
Problem:
Add a function named circle to the polygons module. This function expects the
same arguments as the square and hexagon functions. The function should draw a
circle. (Hint: the loop iterates 360 times.)
Solution:

    ....
"""
import turtle
bob = turtle.Turtle()
def polygon(t,length,n):
   for i in range(n):
      t.fd(length)
      t.lt(360/n)
   print(t)

polygon(bob,30,15)

turtle.mainloop()