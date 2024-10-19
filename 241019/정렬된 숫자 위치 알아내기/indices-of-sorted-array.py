class Number():
    def __init__(self, n, num):
        self.n = n
        self.num = num

N = int(input())
n_list = list(map(int, input().split()))
result = []

for i in range(N):
    result.append(Number(n_list[i], i+1))

original = [x.num for x in result]
result.sort(key= lambda x:(x.n, x.num))

for i in original:
    for j in range(N):
        if i == result[j].num:
            print(j+1, end = ' ')