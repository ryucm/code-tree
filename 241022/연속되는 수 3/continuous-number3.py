N = int(input())

max_cnt = 1
previous_num = 0
cnt = 1
for i in range(N):
    n = int(input())
    if n > 0 and previous_num > 0:
        cnt += 1
    elif n > 0 and previous_num < 0:
        cnt = 1
    elif n < 0 and previous_num < 0:
        cnt += 1
    elif n < 0 and previous_num > 0:
        cnt = 1
    
    previous_num = n
    max_cnt = cnt if cnt > max_cnt else max_cnt

print(max_cnt)