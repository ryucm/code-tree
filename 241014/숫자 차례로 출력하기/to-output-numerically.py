def forward(n):
    if n == 0:
        return

    forward(n-1)
    print(n, end=" ")
    


def reverse(n):
    if n == 0:
        return
    
    print(n, end= " ")
    reverse(n-1)

n = int(input())
forward(n)
print("")
reverse(n)