N = int(input())

arr = sorted(list(map(int,input().split())), reverse=True)

group_max = 0
for i in range(N):
    # i번째와 2n - 1 - i번째 원소를 매칭합니다.
    group_sum = arr[i] + arr[2*N - 1 - i]
    if group_sum > group_max:
        # 최댓값을 갱신합니다.
        group_max = group_sum

print(group_max)