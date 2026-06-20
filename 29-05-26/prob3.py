n=int(input())
t=tuple(map(int,input().split()))
for i in range(n):
    prod=t[0]*t[-1]
print(prod)
