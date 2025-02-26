#Author: Maksym
#Date Modified: Feb 27, 2025
#Description: Math Operators
import math

#This is an adding function
sum_add = 2+23
print("This is result of adding 2+23: " + str(sum_add))
#This is a subtraction function
difference = 2-23
print("This is result of subtructing 2-23: " + str(difference))
#This is a multiplication function
product = 2*3*4
print("This is result of multiplication 2×3×4: " + str(product))
#This is a devision function
quotient = 24/8
print("This is result of devision 24/8: " + str(quotient))
#This is a square root function
square = math.sqrt(25)
print("This is result of square rooting 25: " + str(square))
#This is an exponent function
exponent = 2**4
print("This is result of exponenting 2^4: " + str(exponent))
#This is a remainder function
remainder = 24%5
print("This is result of remainding 24%5: " + str(remainder))

#Descriminant
print("This program will help you to find descriminant!") #Explanation
print("So I just need some information from you")

a = int(input("Please enter a value: ")) #Input
b = int(input("Please enter b value: ")) #Input
c = int(input("Please enter c value: ")) #Input

if a == 0: #Error check
    print("Error, a can't be negative")
else:
    discriminant = math.sqrt(int(b**2-4*a*c)) #Equesion
    print(f"Discriminant = {(discriminant)}") #Output

#Volume of the cone
print("This program will help you to find volume of the cone!") #Explanation
print("So I just need some information from you")

r = float(input("Please enter rarius of the cone: ")) #Input
h = float(input("Please enter height of the cone: ")) #Input

if r <= 0 or h <= 0: #Error check
    print("Error")
else:
    cone_volume = float(math.pi*h*r**2/3) #Equesion
    volume_rounded = round(cone_volume, 2) #Rounding to 2 decimal places
    print(f"Volume = {(volume_rounded)} units\u00b3") #Output

#Volume of the sphere
print("This program will help you to find volume of the sphere!")
print("So I just need to know rarius")

r = float(input("Please enter rarius of the cone: ")) #Input
if r <= 0: #Error check
    print("Error, radius can't be negative or equel to 0")
else:
    sphere_volume = float((4/3)*math.pi*r**3) #Equesion
    volume_rounded = round(sphere_volume, 2) #Rounding to 2 decimal places
    print(f"Volume = {(volume_rounded)} units\u00b3") #Output

#Surface area of the cylinder
print("This program will help you to find surface area of the cylinder!")
print("So I just need some information from you")

r = float(input("Please enter rarius of the cylinder: ")) #Input
h = float(input("Please enter height of the cylinder: ")) #Input

if r <= 0 or h <= 0: #Error check
    print("Error")
else:
    cylinder_sa = float(2*math.pi*r**2 + 2*math.pi*r*h) #Equesion
    sa_rounded = round(cylinder_sa, 2) #Rounding to 2 decimal places
    print(f"Surface area = {(sa_rounded)} units\u00b3") #Output

#Surface area of the triangular prism
print("This program will help you to find the surface area of a triangular prism!")
print("So I just need some information from you")

b = float(input("Please enter the base of the prism: "))   # Input
l = float(input("Please enter the length of the prism: ")) # Input

if b <= 0 or l <= 0:  # Error check
    print("Error: The base and length must be greater than zero!")
else:
    prism_sa = 2 * (math.sqrt(3) / 4) * b**2 + 3 * b * l  # Equation
    sa_rounded = round(prism_sa, 2)  # Rounding to 2 decimal places
    print(f"Surface area = {sa_rounded} units\u00b2")  # Output
