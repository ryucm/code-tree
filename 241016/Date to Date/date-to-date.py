m1, d1, m2, d2 = tuple(map(int, input().split()))

calender = [31, 28, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]
if m1 == m2:
    print((sum(calender[:m2]) + d2) - (sum(calender[:m1]) +d1)+ 1)
else:
    print((sum(calender[:m2]) + d2) - (sum(calender[:m1]) +d1))