#Question two
#Using a function create  a program that calculates the volume of the cylinder

#Solution
radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))
pi = 3.14
volume = pi * (radius** 2)*height

volume = print(f"The volume of the cylinder is : {volume:.3f}")