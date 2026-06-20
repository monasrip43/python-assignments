'''
* problem statement:*
given a integer array arr of size N,
find the count of of elements whose values is
greater than all of its prior elements .
the 1st element is always considered in the count.
'''
n=int(input())
arr=list(map(int, input().split()))
count=1
max_num=arr[0]
for i in range(1,len(arr)):
    if arr[i] >max_num:
        count+=1
        print(count)