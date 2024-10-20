N, K = tuple(map(int, input().split()))
result = [0]*N

for i in range(K):
    A, B = tuple(map(int, input().split()))
    for j in range(A-1, B):
        result[j] += 1

print(max(result))