arr = [[0] * 2001 for _ in range(2001)]
offset = 1000

for i in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    for x in range(x1 + offset, x2 + offset):
        for y in range(y1 + offset, y2 + offset):
            
            if i != 1:
                arr[x][y] += 1
                # print(x, y)
            else:
                arr[x][y] = 0
                # if x > 980 and y > 983:
                #     print(x, y, arr[x][y])

result_x = 0
result_y = 0
for x in range(2001):
    cnt = 0
    for y in range(2001):
        if arr[x][y] != 0:
            # print(arr[x][y], x, y)
            cnt += 1
            # print(x, y ,cnt)
    result_x = result_x + 1 if cnt > 0 else result_x
    result_y = cnt if cnt > result_y else result_y

print(result_x * result_y)