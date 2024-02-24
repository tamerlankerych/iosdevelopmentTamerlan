#ex1
import math

inp = int(input())

out = math.radians(inp)
print(out)

#ex2
import math
height = int(input())
first_v = int(input())
second_v = int(input())
print((first_v + second_v) * height / 2)

#ex3
import math
num_of_sides = int(input())
length_of_side = int(input())
if num_of_sides == 3:
    area = length_of_side ** 2 * math.sqrt(3)/4
    print(f"The area of the polygon is: {area}")
elif num_of_sides == 4:
    area = length_of_side ** 2
    print(f"The area of the polygon is: {area}")
else:
    p = num_of_sides * length_of_side / 2
    apothem = math.sqrt(length_of_side ** 2 - (length_of_side/2) ** 2)
    print(f"The area of the polygon is: {p * apothem / 2}")

#ex4
length_of_base = int(input())
height = int(input())
print(length_of_base * height)