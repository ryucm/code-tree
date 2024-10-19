class F():
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number

n = int(input())
result = []

for i in range(1, n+1):
    x, y = tuple(map(int, input().split()))
    result.append(F(x, y, i))

result.sort(key=lambda x: x.x + x.y)
for i in result:
    print(f"{i.number}")