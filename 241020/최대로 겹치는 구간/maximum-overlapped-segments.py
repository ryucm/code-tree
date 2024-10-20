n = int(input())
arr = [0] * 100
for i in range(n):
    x1, x2 = tuple(map(int, input().split()))
    for i in range(abs(x1), abs(x2)):
        arr[i] += 1

print(max(arr))