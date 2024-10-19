def f(n):
    if n // 2 == 0:
        return str(n % 2)
    return f(n // 2) + str(n % 2)

N = input()
num = 0

for i in N:
    num = num * 2 + int(i)

print(f(num * 17))