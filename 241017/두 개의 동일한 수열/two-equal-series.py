input()

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

if A == B:
    print("Yes")
else:
    print("No")