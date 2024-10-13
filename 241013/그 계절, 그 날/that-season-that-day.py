y, m, d = tuple(map(int, input().split()))


def is_leap_year(y):
    if y % 4 != 0:
        return False
    
    if y % 100 != 0:
        return True
    
    if y % 400 == 0:
        return True
    
    return False


def is_exist_day(y, m, d):
    num_of_days = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    num_of_days[2] = 29 if is_leap_year(y) else 28

    return d <= num_of_days[m]

   
if not is_exist_day(y, m, d):
    print(-1)
else:
    if 3 <= m and m <= 5:
        print("Spring")
    elif 6 <= m and m <= 8:
        print("Summer")
    elif 9 <= m and m <= 11:
        print("Fall")
    else:
        print("Winter")