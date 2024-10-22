def f(n):
    arr, pos = [0], 1
    for _ in range(n):
        v, t = tuple(map(int, input().split()))
        for i in range(t):
            arr.append(arr[pos-1] + v)
            pos += 1
    return arr

N, M = tuple(map(int, input().split()))

arr_A, arr_B = f(N), f(M)

cnt = 0
winner = ''
    
# print(arr_A[:20])
# print(arr_B[:20])
for i in range(len(arr_A)):
    # print(winner)
    if arr_A[i] != arr_B[i] and winner == '':
        winner = 'A' if arr_A[i] > arr_B[i] else 'B'
    elif arr_A[i] == arr_B[i] and winner == '':
        continue
    
    if arr_A[i] + arr_A[i-1] > arr_B[i] + arr_B[i-1]:
        if winner == 'A':
            continue
        else:
            winner = 'A'
            cnt += 1
    elif arr_A[i] + arr_A[i-1] < arr_B[i] + arr_B[i-1]:
        if winner == 'B':
            continue
        else:
            winner = 'B'
            cnt += 1
            

print(cnt)