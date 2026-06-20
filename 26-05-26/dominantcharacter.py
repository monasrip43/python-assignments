s=input()
max_len=0
for i in range(len(s)):
    freq={}
    for j in range(i,len(s)):
        ch=s[j]
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
        max_freq=max(freq.values())
        length=j-i+1
        if max_freq>length-max_freq:
            if length>max_len:
                max_len=length
print(max_len)