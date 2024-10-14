n, m = tuple(map(int, input().split()))

A = list(map(int, input().split()))

def cal(arr , num):
    result = 0
    while num >= 1:
        result += arr[num -1]
        if num % 2 != 0:
            num -= 1
        else:
            num = int(num / 2)
    return result

print(cal(A, m))