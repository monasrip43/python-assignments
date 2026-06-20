n=int(input())
l=list(map(int,input().split()))
m=int(input())
a=list(map(int,input().split()))
merged=[]
i=j=0
while i<n and j<m:
    if l[i]<a[j]:
        merged.append(l[i])
        i+=1
    else:
        merged.append(a[j])
        j+=1
merged.extend(l[i:])
merged.extend(a[j:])
print(merged)