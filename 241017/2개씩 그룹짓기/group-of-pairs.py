N = int(input())

arr = sorted(list(map(int,input().split())), reverse=True)

print(arr[(len(arr) - (len(arr) // 2))] + arr[(len(arr) - (len(arr) // 2)) -1])