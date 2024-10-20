n = int(input())
arr = [0] * 100
for i in range(n):
    x1, x2 = tuple(map(int, input().split()))
    if x1 < 0:
        x1 += -x1
        x2 = -x1 + x2
    elif x2 < 0:
        x1 = -x2 + x1
        x2 += -x2
    for i in range(x1, x2):
        arr[i] += 1

print(max(arr))