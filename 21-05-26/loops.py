'''
what is a loop?
  A loop is used to repeat the block of code
  instead of writing the logics again and again
  we will repeat the code

'''

#looping statements are 2 types
#      /           \
#    For          while
'''
for ---> used when num of iterations(one cycle) are known
while ---> num of iterations are unknown and executes until the condition is true

Benifits
1. reduces the code duplications and complexities
2. saves time
3. make your program very efficient
4. helps in the automation 

             execution flow of loops 
                     START
                       |
                    condition check
                        |
                    True ---> Executes the block
                        |
                     Repeat
                        |
                     False---> stop

'''
# For loop : it iterates on the sequences
#list,tuples,range,strings
'''
in C-programming
 for (i=0; i<n; i++){
 i=0 ---> intialization
 i<n ---> condition
 i++ ---> increment
 }



 # in Python 
 list ---> collection of operand elements
 list ---> [,,,]
 it doesnot have limitations
 list is immutable
'''
'''
frnds = ["meghs","mouns","haars"]

#syntax:
#for var in sequence:
# statements

for frnd in frnds:
    print(frnd)
'''
#2nd way?
#range (start, end-1, step)
#range(1,11)
'''
for i in range(5):
    print(i)
for i in range(1,16):
    print(i)
'''
# Multiplication table of 5
'''
for i in range(1,11):
    a=5*i
    print(a)
'''
   # 2nd method
'''
num = 5
for i in range(1,11):
    print(num, "x",i, "=",num*i )
'''
#sum of numbers (1,6)
'''
num = 0
for i in range(1,6):
      num = num+i
      print(num)
      '''

# s= "mona" now count character in your name using for loop
'''
s="mona"
char_count = {}
for i in s:
    if i in char_count:
       char_count[i]+=1
    else:
        char_count[i] = 1
print(char_count)
'''

#use for loop and print only
# even numbers upto 20
#dont write even num logic
'''
for i in range(2,21,2):
    print(i)
'''
#reverse of the sequence
'''
for i in range(11,0,-1):
    print(i)
'''
#while loop 
#syntax
'''
while condition 
  statement
  example 
   i=1 
    while i<=5:
    print(i)
    i+=1  #if the increment is not given then it loops for infinite times
'''

#infinite loop
'''
while True:
    print("run forevere")
'''
#sum of numbers using while
#do sum until the input is 0
'''
num = int(input())
total = 0
while num != 0:
    total+=num
    num=int(input())
    '''
#2nd method
'''
num = int(input())
total = 0
while num != 0:
    total=total+num
    num=int(input())
print(total)
'''
#print the even numbers from 2 to 20
'''
starts from 2
      |
checks if num<=20
      |
print(num)
      |
increment the number by 2
      |
   Repeat
      |
   stop after 20
'''
'''
i = 0
while i<=20:
    if i%2==0:
        print(i)
        i+=2
'''
