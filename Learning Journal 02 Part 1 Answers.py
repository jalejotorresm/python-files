#First, I will use a piece of code I read on the Section 3.2 of our textbook (Downey, 2015, p.18)

import math #This code will import the math module within Python

#Second, I will define the print_volume function
def print_volume(r):
    print((4/3)*math.pi*(r**3))
    print()

#Finally, I will call the function with 3 values: an integer, an expression and a float
print('Basic Sphere Volume Calculator')
print()

print('First Sphere Volume calculation with r=3')
print_volume(3)

print('Second Sphere Volume calculation with r=4/3')
print_volume(4/3)

print('Third Sphere Volume calculation with r=85.77')
print_volume(85.77)

#References:
#Downey, A. (2014). Think Python. How to Think Like a Computer Scientist. Second Edition, Version 2.2.23. Needham, Massachusetts: Green Tea Press.

