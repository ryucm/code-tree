def f(n, b):
    if n // b == 0:
        return str(n % b)
    return f(n // b, b) + str(n % b)

N, B = tuple(map(int, input().split()))

print(f(N, B))