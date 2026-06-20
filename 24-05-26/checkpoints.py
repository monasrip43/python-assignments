checkpoint=int(input())
energy=0
for i in range(1,checkpoint+1):
    if i%2==0:
        energy+=5
    if i%3==0:
        energy-=2
print(energy)
