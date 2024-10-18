class Product():
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code

name, code = input().split()

a = Product()
b = Product(name, code)

print(f"product {a.code} is {a.name}")
print(f"product {b.code} is {b.name}")