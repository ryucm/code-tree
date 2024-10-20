N, K = tuple(map(int, input().split()))
result = [0]*N

for i in range(K):
    A, B = tuple(map(int, input().split()))
    for j in range(A, B+1):
        result[j] += 1

print(max(result))