n, m = tuple(map(int, input().split()))
A = list(map(int, input().split()))

for _ in range(m):
    a1, a2 = tuple(map(int, input().split()))
    print(sum(A[a1 - 1: a2]))