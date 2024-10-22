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
    if arr_A[i] > arr_B[i]:
        if winner == 'B':
            cnt +=1
        winner = 'A'
    elif arr_A[i] < arr_B[i]:
        if winner == 'A':
            cnt += 1
        winner = 'B'
            
print(cnt)