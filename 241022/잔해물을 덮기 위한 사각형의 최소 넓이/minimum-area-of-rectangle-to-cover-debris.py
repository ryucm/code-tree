arr = [[0] * 2001 for _ in range(2001)]
offset = 1000

for i in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    for x in range(x1 + offset, x2 + offset):
        for y in range(y1 + offset, y2 + offset):
            
            if i != 1:
                arr[x][y] += 1
            else:
                arr[x][y] == 0

result_x = 0
result_y = 0
for x in range(len(arr)):
    cnt = 0
    for y in range(x):
        if arr[x][y] == 1:
            cnt += 1
    result_x = result_x + 1 if cnt > 0 else result_x
    result_y = cnt if cnt > result_y else result_y

print(result_x * result_y)