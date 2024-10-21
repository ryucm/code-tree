N = int(input())

max_cnt = 1
cnt = 1
previous_num = 0

for i in range(N):
    n = int(input())

    if previous_num < n:
        cnt += 1
    else:
        cnt =1
    previous_num = n
    max_cnt = max_cnt if cnt < max_cnt else cnt
print(max_cnt)