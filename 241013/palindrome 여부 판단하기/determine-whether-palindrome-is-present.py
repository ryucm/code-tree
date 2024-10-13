A = input()

def is_palindrome(string):
    return string[::-1]

temp = is_palindrome(A)
if A == temp:
    print("Yes")
else:
    print("No")