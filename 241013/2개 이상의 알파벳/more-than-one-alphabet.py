A = input()

def is_dupl(A):
    count = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                pass
            if A[i] != A[j]:
                count += 1
    return count

if is_dupl(A):
    print("Yes")
else:
    print("No")