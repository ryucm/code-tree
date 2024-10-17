n, k, T = list(input().split())

arr = []

for _ in range(int(n)):
    temp = input()
    th = True
    for i in range(len(T)):
        if temp[i] != T[i]:
            th = False
            break
    if th:
        arr.append(temp)
arr.sort()
print(arr[int(k)-1])