def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_recursive(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return lcm(numbers[0], lcm_recursive(numbers[1:]))

input()
print(lcm_recursive(list(map(int, input().split()))))