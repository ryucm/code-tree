n, m = tuple(map(int, input().split()))
arr = [[0, 0] for i in range(100)]
cur_A = 0
cur_B = 0

time_A = 0

for i in range(n):
    t, d = input().split()

    for _ in range(int(t)):                    
        if d == 'L':
            cur_A -= 1
            arr[time_A][0] = cur_A
        else:
            cur_A += 1
            arr[time_A][0] = cur_A
        time_A += 1

time_B = 0
for i in range(m):
    t, d = input().split()

    for _ in range(int(t)):                    
        if d == 'L':
            cur_B -= 1
            if time_B > time_A:
                arr[time_B] = [cur_A, cur_B]
            else:
                arr[time_B][1] = cur_B
        else:
            cur_B += 1
            if time_B > time_A:
                arr[time_B] = [cur_A, cur_B]
            else:
                arr[time_B][1] = cur_B
        time_B += 1

cnt = 0
for i in range(1, max(time_A, time_B)):
    if arr[i][0] == arr[i][1]:
        if arr[i-1][0] != arr[i-1][1]:
            # print(arr[i], i)
            cnt+=1

print(cnt)