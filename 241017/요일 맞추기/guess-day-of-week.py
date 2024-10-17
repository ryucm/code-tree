calender = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = tuple(map(int, input().split()))
diff = sum(calender[:m2]) + d2 - sum(calender[:m1]) - d1

print(week[diff % 7])