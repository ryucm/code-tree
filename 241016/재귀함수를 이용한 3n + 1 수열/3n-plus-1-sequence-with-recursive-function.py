def f(n):
    if n == 1:
        return 0
    
    if n % 2 ==0:
        n = n // 2
    else:
        n = n * 3 + 1
    
    return f(n) + 1

n = int(input())
print(f(n))