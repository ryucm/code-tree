N = int(input())

arr = sorted(list(map(int,input().split())), reverse=True)

print(arr[1] + arr[-2])