n=int(input())
l=list(map(int,input().split()))
k=int(input())
left=0
right=len(l)-1
closest_pair=(l[left],l[right])
while left<right:
    current_sum=l[left]+l[right]
    if abs(current_sum-k)<abs(sum(closest_pair)-k):
        closest_pair=(l[left],l[right])
    if current_sum<k:
        left+=1
    else:
        right-=1
print(*closest_pair)