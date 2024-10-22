N, M = tuple(map(int, input().split()))
arr_A = [0] * 1001
arr_B = [0] * 1001
cur_A = 0
cur_B = 0

for i in range(N):
    v, t = tuple(map(int, input().split()))

    for i in range(cur_A+1, t+cur_A+1):
        arr_A[i] = arr_A[i-1] + v
        cur_A += 1
for i in range(M):
    v, t = tuple(map(int, input().split()))

    for i in range(cur_B+1, t+cur_B+1):
        arr_B[i] = arr_B[i-1] + v
        cur_B += 1

cnt = 0
previous_value = ''
for i in range(1001):
    temp = ''
    if arr_A[i] + arr_A[i-1] == arr_B[i] + arr_B[i-1]:
        continue

    if previous_value == '':
        previous_value = 'A' if arr_A[i] > arr_B[i] else 'B'
        continue
    
    if arr_A[i] + arr_A[i-1] > arr_B[i] + arr_B[i-1]:
        if previous_value == 'A':
            continue
        else:
            previous_value = 'A'
            cnt += 1
    elif arr_A[i] + arr_A[i-1] < arr_B[i] + arr_B[i-1]:
        if previous_value == 'B':
            continue
        else:
            previous_value = 'B'
            cnt += 1
            
    
# print(arr_A[:20])
# print(arr_B[:20])
print(cnt)