def max_f(n, m):
    if n > m:
        return n
    else:
        return m

def min_f(n, m):
    if n < m:
        return n
    else:
        return m

N = int(input())
square = [[0]*201 for _ in range(201)]
offset = 100

cnt = 0
for i in range(N):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    for x in range((x1 + offset), (x2 + offset)):
        for y in range((y1 + offset), (y2 + offset)):
            if square[x][y] == 1:
                continue

            square[x][y] = 1
            cnt += 1
            # print(x, y, cnt)

print(cnt)