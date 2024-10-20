n = int(input())
arr = [0] * 101
for i in range(n):
    x, y = tuple(map(int, input().split()))

    for j in range(x, y+1):
        arr[j] += 1
print(max(arr))