n = int(input())
for i in range(n):
    for j in range(n):
        
        # Main diagonal or secondary diagonal
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print("-", end="")
    
    print()