N = int(input())

arr = sorted(list(map(int,input().split())), reverse=True)

for i in range(1, len(arr)):
    if arr[0] != arr[i]:
        print(arr[0] + arr[i])
        break