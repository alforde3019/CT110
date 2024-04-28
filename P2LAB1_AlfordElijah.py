import math

area = 3.14159 * 5**2
radius = float(input('What is the radius of the circle? '))

diameter = 2*(radius)
print("The diameter of circle is:", round(diameter,1))

circumference = 2 * math.pi * (radius)
print("The circumference of circle is:", round(circumference,2))

area = math.pi * (radius)**2
print("The area of circle is:", round(area,3))

