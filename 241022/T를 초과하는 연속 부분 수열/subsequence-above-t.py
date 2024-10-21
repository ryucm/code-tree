n, t = map(int, input().split())
N = list(map(int, input().split()))

max_cnt = 0
cnt = 0
for i in N:
    if i > t:
        cnt += 1
    else:
        cnt = 0
    
    max_cnt = max_cnt if cnt < max_cnt else cnt

print(max_cnt)