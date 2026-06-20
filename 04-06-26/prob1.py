s = (input().strip())

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

counts = list(freq.values())

valid = False

for i in range(len(counts)):
    temp = counts[:]

    temp[i] -= 1

    if temp[i] == 0:
        temp.pop(i)

    if len(temp) == 0:
        valid = True
        break

    if len(set(temp)) == 1:
        valid = True
        break

if len(set(counts)) == 1:
    valid = True

print("YES" if valid else "NO")