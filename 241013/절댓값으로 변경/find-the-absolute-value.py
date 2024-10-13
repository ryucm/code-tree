n = int(input())

num_list = list(map(int, input().split()))

def return_abs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
return_abs(num_list)
print(" ".join(map(str, num_list)))