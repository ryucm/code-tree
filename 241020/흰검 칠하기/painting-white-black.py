n = int(input())

arr = [[0, 0, '']] * (2000 * 100 + 1)
idx = 1000 * 100

for i in range(n):
    x, o = input().split()
    x = int(x)

    if o == 'L':
        for j in range(idx-x+1, idx+1):
            arr[j] = [arr[j][0] + 1, arr[j][1], 'W']
            idx = j
    
    if o == 'R':
        for j in range(idx, idx+x):
            arr[j] = [arr[j][0], arr[j][1] + 1, 'B']
            idx = j

white = black = gray = 0
for i in arr:
    if i[0] >= 2 and i[1] >= 2:
        gray += 1
    elif i[2] == 'W':
        white += 1
    elif i[2] == 'B':
        black += 1

print(white, black, gray)