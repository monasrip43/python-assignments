#take the three inputs from the user and check whether it is 
#1.isosceles-2 sides equal
#2.equilaterial-all sides are equale
#3.scalene-3 different
a=int(input("enter the first side of the triangle:"))
b=int(input("enter the second side of the triangle:"))
c=int(input("enter the third side of the triangle:"))
if a==b==c:
    print("ths triangle is equilaterial")
elif a==b or b==c or a==c:
    print("the triangle is isoscene triangle")
else:
    print("the triangle is scalene")
