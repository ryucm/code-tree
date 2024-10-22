N, M, K = tuple(map(int, input().split()))
students = list(range(1, N+1))
f = [0]*len(students)

result = -1
for i in range(1, M+1):
    num = int(input())

    f[num-1] += 1
    if f[num-1] >= K and result == -1:
        result = num
print(result)