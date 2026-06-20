n = int(input())
arr = list(map(int, input().split()))
k = int(input())
k = k % n
result = arr[-k:] + arr[:-k]
print(*result)