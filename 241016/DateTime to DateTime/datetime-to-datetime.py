a, b, c = tuple(map(int, input().split()))

print((a * 1440 + b * 60 + c) - (11 * 1440 + 11 * 60 + 11))