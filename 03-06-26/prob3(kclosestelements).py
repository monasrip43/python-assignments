n = int(input())
arr = list(map(int, input().split()))
k, x = map(int, input().split())

left = 0
right = n - 1

while right - left + 1 > k:
    if abs(arr[left] - x) > abs(arr[right] - x):
        left += 1
    else:
        right -= 1

print(*arr[left:right + 1])