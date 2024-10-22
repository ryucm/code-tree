N, M, K = tuple(map(int, input().split()))
students = list(range(1, N+1))

result = -1
for i in range(1, M+1):
    num = int(input())

    if num in students and result == -1:
        result = num

print(result)