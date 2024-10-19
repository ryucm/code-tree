a, b = tuple(map(int, input().split()))
n = input()
num = 0

for i in n:
    num = num * a + int(i)

def f(n, b):
    if n // b == 0:
        return str(n % b)
    return f(n // b, b) + str(n % b)

print(f(num, b))