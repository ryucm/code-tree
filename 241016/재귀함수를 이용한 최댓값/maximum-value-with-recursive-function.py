def f(arr, n):
    idx = n-1

    if idx == 0:
        return arr[idx]

    crt_n = arr[idx]
    nxt_n = f(arr, n-1)

    return crt_n if crt_n > nxt_n else nxt_n

num = int(input())
numbers = list(map(int, input().split()))
print(f(numbers, num))