#Author: Maksym
#Date Modified: Feb 21, 2025
#Description: Math Operators
import math
#This is an adding function
sum_add = 2+23
#This is a subtraction function
difference = 2-23
#This is a multiplication function
product = 2*3*4
#This is a devision function
quotient = 24/8
#This is a square root function
square = math.sqrt(25)
#This is a exponent function
exponent = 2**4

#Descriminant
'''
a = int(input("Please enter a value: "))
b = int(input("Please enter b value: "))
c = int(input("Please enter c value: "))

discriminant = math.sqrt(int(
    b**2-4*a*c)
)
print("Discriminant = "+ str(discriminant))
'''
#Volume of the cone
'''
print("This program will help you to find volume of the cone!")
print("So I just need some information from you")

r = float(input("Please enter rarius of the cone: "))
h = float(input("Please enter height of the cone: "))

cone_volume = float(math.pi*h*r**2/3)

volume_rounded = round(cone_volume, 2)

print("Volume = "+ str(volume_rounded) + " units")
'''
#Volume of the sphere
'''
print("This program will help you to find volume of the sphere!")
print("So I just need to know rarius")

r = float(input("Please enter rarius of the cone: "))

sphere_volume = float(4/3*math.pi*r**3)

volume_rounded = round(sphere_volume, 2)

print("Volume = " + str(volume_rounded) + " units")
'''
#Surface area of the cylinder
'''
print("This program will help you to find surface area of the cylinder!")
print("So I just need some information from you")

r = float(input("Please enter rarius of the cylinder: "))
h = float(input("Please enter height of the cylinder: "))

cylinder_sa = float(2*math.pi*r**2 + 2*math.pi*r*h)

volume_rounded = round(cylinder_sa, 2)

print("Volume = " + str(volume_rounded) + " units")
'''