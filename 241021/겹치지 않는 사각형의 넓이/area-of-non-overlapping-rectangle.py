arr = [[0] * 2001 for _ in range(2001)]
offset = 1000

cnt = 0

for i in range(1, 4):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    
    for x in range(x1+offset, x2+offset):
        for y in range(y1+offset, y2+offset):
            arr[x][y] += 1
            if i == 3 and arr[x][y] == 2:
                # print(cnt, x, y, arr[x][y])
                cnt -= 1
            if i == 3:
                continue
            else:
                cnt += 1

print(cnt)