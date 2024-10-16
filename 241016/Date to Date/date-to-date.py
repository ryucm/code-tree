m1, d1, m2, d2 = tuple(map(int, input().split()))

calender = [31, 28, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]
print((sum(calender[:m2-1]) + d2) - (sum(calender[:m1-1]) +d1) +1)