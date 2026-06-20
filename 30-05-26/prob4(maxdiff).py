n = int(input())
arr = list(map(int, input().split()))
min_ele = arr[0]
max_diff = arr[1] - arr[0]
for i in range(1, n):
    if arr[i] - min_ele > max_diff:
        max_diff = arr[i] - min_ele
    if arr[i] < min_ele:
        min_ele = arr[i]
print(max_diff)