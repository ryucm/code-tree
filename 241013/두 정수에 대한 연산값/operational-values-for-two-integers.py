a, b = tuple(map(int, input().split()))

def calculate(n, m):
    n += 25
    m *= 2
    return n, m

if a > b:
    a, b = calculate(a, b)
else:
    b, a = calculate(b, a)

print(a, b)