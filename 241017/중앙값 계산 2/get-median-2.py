n = int(input())
arr = list(map(int, input().split()))

result = []

for i in range(1, n+1):
    if i % 2 != 0:
        result.append(sorted(arr[:i])[(i-1) // 2])
print(" ".join(map(str,result)))