a, b, c = tuple(map(int, input().split()))
result = (a * 1440 + b * 60 + c) - (11 * 1440 + 11 * 60 + 11)
print(result if result >= 0 else -1)