N = int(input())

arr = [[0] * 201 for _ in range(201)]
offset = 100
cnt = 0

for i in range(N):
    x1, y1 = tuple(map(int, input().split()))

    for x in range(x1, x1+8):
        for y in range(y1, y1+8):
            arr[x][y] += 1
            if arr[x][y] == 1:
                cnt +=1

print(cnt)