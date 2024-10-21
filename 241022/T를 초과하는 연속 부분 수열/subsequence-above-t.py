n, t = map(int, input().split())
N = list(map(int, input().split()))

max_cnt = 0
cnt = 0
previous_num = 0
for i in N:
    if i > t and previous_num < i:
        cnt += 1
    else:
        cnt = 0
    
    previous_num = i
    max_cnt = max_cnt if cnt < max_cnt else cnt

print(max_cnt)