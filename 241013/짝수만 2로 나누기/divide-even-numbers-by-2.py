n = int(input())
n_ls = list(map(int, input().split()))

def modify(arr, n_len):
    for i in range(n_len):
        if arr[i] % 2 == 0:

            arr[i] = int(arr[i] / 2)

modify(n_ls, n)
print(" ".join(map(str, n_ls)))