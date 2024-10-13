a, b = tuple(map(int, input().split()))

def calculate(n, m):
    n *= 2
    m += 10
    return n, m

if a > b:
    a, b = calculate(a, b)
else:
    b, a = calculate(b, a)

print(a, b)