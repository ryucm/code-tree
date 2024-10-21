arr = [[0] * 2001 for _ in range(2001)]
offset = 1000

for i in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    for x in range(x1 + offset, x2 + offset):
        for y in range(y1 + offset, y2 + offset):
            
            if i != 1:
                arr[x][y] += 1
            else:
                arr[x][y] = 0

max_x = max_y = 0
min_x = min_y = 2002
for x in range(2001):
    cnt = 0
    for y in range(2001):
        if arr[x][y] != 0:
            cnt += 1
            max_y = y if y > max_y else max_y
            min_y = y if y < min_y else min_y

    max_x = x if cnt > 0 and x > max_x else max_x
    min_x = x if cnt > 0 and x < min_x else min_x
    
print((max_x-(min_x-1)) * (max_y-(min_y-1)) if max_x or max_y else 0)