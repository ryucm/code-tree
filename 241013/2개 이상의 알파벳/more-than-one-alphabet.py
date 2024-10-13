A = input()

def is_dupl(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                pass
            if A[i] == A[j]:
                return True
    return False

if is_dupl:
    print("Yes")
else:
    print("No")