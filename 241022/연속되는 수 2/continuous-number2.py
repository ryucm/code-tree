N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

max_x = 0
cnt = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        cnt += 1
        max_x = max_x if cnt < max_x else cnt
    else:
        cnt = 1

print(max_x)