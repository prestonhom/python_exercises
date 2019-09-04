# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
a = int(input("Please enter length of a "))
b = int(input("Please enter length of b "))
c = int(input("Please enter length of c "))


if(a == b and a == c):
    print(f"A triangle with sides {a}, {b}, {c} is an equilateral triangle ")
elif(a != b and a != c and b != c):
    print(f"A triangle with sides {a}, {b}, {c} is a scalene triangle ")
elif((a == b and a != c) or (b == c and b != a)):
    print(f"A triangle with sides {a}, {b}, {c} is an isoceles triangle ")