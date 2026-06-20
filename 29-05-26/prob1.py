size=int(input())
n=list(map(int,input().split()))
even_sum=0
odd_sum=0
for i in range(size):
    if i%2==0:
        even_sum+=n[i]
    else:
        odd_sum+=n[i]
print(even_sum,odd_sum)