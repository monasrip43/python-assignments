'''
Nested loop: loop inside a loop

first loop : outer loop ---> row
second loop : inner loop --> column
'''
#example
'''
i = 1
while i<= 3:
    j=1
    while j<=2:
        print(i,j)
        j=j+1
    i=i+1 
    '''
'''
for loop :
for outer in range():
for inner in range():
 #code
 for every row :
    for every student in that row:
    #greet the student
How nested loop works using the for loop
for i in range(1,4): #i=1 2 3 
 for j in range(1,3): #j=1 2 1 2 1 2
 print(i,j)

 outer loop runs once 
    inner loop runs completely
 outer loop runs twice
    inner loop runs completely
'''

'''
why nested loops are used?
 1. pattern problems
 2. matrix operation 
 3. tables
 4. games
 5. grid systems
 6. comparing the elements
'''
'''
#square - star patterns
****
****
****
****
'''
'''
for i in range(1,5):
    for j in range(1,5):
       print("*",end="") # if we use end in the print statement we can print the output vertically
    print()
'''

#example 2 : right angle triangle
'''
*
**
***
****
*****
'''
'''
for i in range(6):
    for j in range(0,i):
        print("*",end=" ")
    print()
'''

#example 3 : Number pattern
'''
 1
 1 2
 1 2 3
 1 2 3 4
 1 2 3 4 5
 '''
'''
for i in range(1,6):
     for j in range(1,i+1):
        print(j,end=" ")
     print()
'''

'''
*****
****
***
**
*
'''
'''
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
'''
#example 5
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
'''
n= int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
'''

'''
#ex-6
5 4 3 2 1
5 4 3 2
5 4 3
5 4 
5                          

'''
'''
n=int(input())
for i in range(n):
    for j in range(n,i,-1):
        print(j,end=" ")
    print()
'''
'''
example 7
A
B C
D E F
G H I J

chr() is used to convert ascii values to alphabets
'''
'''
a=int(input())
for i in range(1,5):
    for j in range(i):
        print(chr(a),end=" ")
        a+=1
    print() 
''' 

'''
1
1 3
1 3 5
1 3 5 7


odd=2*n-1
'''
'''
n=int(input())
for i in range(1,n):
    for j in range(1,i,2):

    


    
'''
'''
    *
   * *
  * * * 
 * * * *
* * * * *   
'''
n=int(input())

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()