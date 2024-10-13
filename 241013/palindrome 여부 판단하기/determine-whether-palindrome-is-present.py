A = input()

def palindrome(string):
    return string[::-1]

temp = palindrome(A)
if A == temp:
    print("Yes")
else:
    print("No")