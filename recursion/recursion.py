'''
what is recursion?
a function calls itself to solve a problem.
 
the recursion is used to deal with the problems like repetitive tasks and hierarchical structures.

example :
with the recursion:
def hello():
print("hello")
hello()


'''
# def hello():
#    print("Hello world")
# hello()

# def hello(n):
#    if n==0: #base condition 
#       return
#    print("hello")
#    hello(n-1)
# hello(5)

'''
how recursion works in python?
recursion works by allowing a function to call itself with modified arguments.


'''
#to calculate the sum using recursion:
# def sum(num):
#    if num == 1: #base case
#       return num
#    return num + sum(num-1) #recursive case
# print(sum(3)) #3+2+1
'''
sum(3) calls sum(2) #3
sum(2) calls sum(1) #2
sum(1) returns 1(base case)#1
3+2+1=6

'''
'''
call stack :last in first out(LIFO)

'''
# def fun1():
#   print("function1")

# def fun2():
#     print("func2")

# fun1()
# fun2()


#factorial of a number:
'''
n!=5!=5*(5-1)*(5-2)*...*1

n!=n*(n-1)!
'''
# def factorial(num):
#     if num == 0: #base case
#         return 1
#     return num*factorial(num-1)#recursive case
# print(factorial(4))#4*3*2*1

'''
fact(1)    |pop 1
fact(2)     pop 1*2
fact(3)     pop 1*2*3
fact(4)     pop 1*2*3*4

'''
#common issues :
#1.exceeding the maximum recursion depth
#2.missing the base case

'''
when do we use recursion?
1.to divide them into subproblems
2. when we have the hierarchical structures
3.code reliability
4.code reusability

'''

#fibonacci series:
# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)#4+3=7
# print(fib(5))

#reverse of a string:
# def reverse(n):
    # if len(n)==0:
        # return""
    # return reverse(n[1:])+n[0]
# print(reverse("hello"))
'''
h e l l o
0 1 2 3 4
olleh             n[1:]      n[0]  returns
1. "hello"        "ello"      h        ello +h
2.  ello             llo       e         llo+e
3    llo              lo       l          lo+l
4.   lo               o        l           o+l
5.    o             ""        o            o

returns""
returns"o"
returns"l"
returns"l"
returns"e"
returns"h"
'''