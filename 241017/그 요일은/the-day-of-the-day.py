calender = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = tuple(map(int, input().split()))
week = input()

diff = sum(calender[:m2]) + d2 - sum(calender[:m1]) - d1
print(diff // 7 + 1 if diff % 7 >= 4 else diff // 7)