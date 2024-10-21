n = int(input())
arr = [[0] * 201 for _ in range(201)]
offset = 100

for i in range(1, n+1):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    for x in range(x1 + offset, x2 + offset):
        for y in range(y1 + offset, y2 + offset):
            if i % 2 != 0:
                arr[x][y] = 0
            else:
                arr[x][y] = 1

cnt = 0
for x in range(201):
    for y in range(201):
        cnt += arr[x][y]

print(cnt)