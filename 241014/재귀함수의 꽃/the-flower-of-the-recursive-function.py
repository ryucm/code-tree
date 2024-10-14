def recursive(n):
    if n == 0:
        return
    print(n, end=" ")
    recursive(n-1)
    print(n, end=" ")
    

recursive(int(input()))