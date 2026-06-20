A=input()
B=input()
freq={}
freq1={}
for i in range(len(A)):
    ch=A[i]
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for j in range(len(B)):
    ch1=B[j]
    if ch1 in freq1:
        freq1[ch1]+=1
    else:
        freq1[ch1]=1
if freq==freq1:
    print("YES")
else:
    print("NO")