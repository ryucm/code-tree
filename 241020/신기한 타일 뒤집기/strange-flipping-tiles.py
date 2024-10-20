n = int(input())

arr = [0] * (2 * 1000 * 100 + 1)
idx = 1000 * 100

for i in range(n):
    x, o = input().split()
    x = int(x)

    if o == 'L':
        for j in range(idx-x+1, idx+1):
            # print(j, 'W')
            arr[j] = -1
        idx -= x+1
        print(idx)
    
    else:
        for j in range(idx, idx+x):
            # print(j, 'B')
            arr[j] = 1
        idx += (x-1)
        # print(idx)

white = 0
black = 0

for i in arr:
    if i == -1:
        white += 1
    elif i == 1:
        black += 1

print(white, black)