n = int(input())
arr = [0] * 200
for i in range(n):
    x1, x2 = tuple(map(int, input().split()))
    
    for i in range(x1 + 100, x2 + 100):
        arr[i] += 1

print(max(arr))