s=input()
vowels=0
consonants=0
for i in s:
    if i.isalpha():
        if i in "aeiou":
            vowels+=1
        else:
           consonants+=1
if vowels==consonants:
    print("Balanced")
else:
    print("Not Balanced")