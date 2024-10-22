N, M = tuple(map(int, input().split()))
arr_A = []
arr_B = []
cur_A = cur_B =0

for i in range(N):
    d, t = input().split()
    if d == 'L':
        for j in range(cur_A-1, (int(t) * -1)+cur_A-1, -1):
            arr_A.append(j)
            cur_A -= 1
            # print(cur_A, j, 'L')
    else:
        for j in range(cur_A+1, int(t)+cur_A+1):
            arr_A.append(j)
            cur_A += 1
            # print(cur_A, j, 'R')

for i in range(M):
    d, t = input().split()
    if d == 'L':
        for j in range(cur_B-1, (int(t) * -1)+cur_B-1, -1):
            arr_B.append(j)
            cur_B -= 1
    else:
        for j in range(cur_B+1, int(t)+cur_B+1):
            arr_B.append(j)
            cur_B += 1

# print(arr_A)
# print(arr_B)
result = -1
for i in range(len(arr_A)):
    if arr_A[i] == arr_B[i]:
        result = i+1
        break

print(result)