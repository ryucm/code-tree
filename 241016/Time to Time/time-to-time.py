a, b, c, d = tuple(map(int, input().split()))

elapsed_time = 0
while True:
    if a == c and b == d:
        break
    
    elapsed_time += 1
    b += 1

    if b == 60:
        b = 0
        a += 1

print(elapsed_time)