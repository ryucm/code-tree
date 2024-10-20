n = int(input())
arr = [0] * n*20
start = 100
for i in range(n):
    x, y = input().split()
    if y == 'L':
        for j in range(start-int(x), start):
            arr[j] += 1
        start -= int(x)
        # print(arr)
    else:
        for j in range(start, start+int(x)):
            arr[j] += 1
        start += int(x)
        # print(arr)
count = 0
for i in arr:
    if i >= 2:
        count += 1
print(count)