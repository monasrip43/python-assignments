 #Divisible by 5
# check whether the given number is divisible by 5 or not
'''
a = int(input("enter the number:"))
if a%5 == 0 :
    print("a is divisible by 5")
else:
    print("a is not divisible by 5")
    '''
#leap year
# it should be divisible by 4 or 400
# should not be divisible by 100

a = int(input("enter the year:"))
if a%400 == 0 or a%4 == 0 and a%100 != 0:
    print(" a is a leap year")
else:
    print("a is not a leap year")