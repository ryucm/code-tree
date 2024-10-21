N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

max_x = 1
cnt = 1
for i in range(len(arr)):
    if i == 0:
        continue
    elif arr[i] == arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    max_x = max_x if cnt < max_x else cnt

print(max_x)