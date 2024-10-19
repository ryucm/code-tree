def f(n):
    if n // 2 == 0:
        return str(n % 2)
    
    return f(n // 2) + str(n % 2)

print(f(int(input())))