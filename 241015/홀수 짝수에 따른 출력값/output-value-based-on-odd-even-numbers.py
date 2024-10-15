def f(n):
    if n <= 2:
        return n
    
    return f(n-2) + n

print(f(int(input())))