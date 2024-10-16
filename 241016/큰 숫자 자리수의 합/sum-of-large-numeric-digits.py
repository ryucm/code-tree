def f(n):
    if n // 10 == 0:
        return n
    
    return f(n // 10) + (n % 10) 

num = list(map(int, input().split()))
print(f(num[0] * num[1] * num[2]))