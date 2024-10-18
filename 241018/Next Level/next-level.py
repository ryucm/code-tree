class User():
    def __init__(self, id='codetree', level=10):
        self.id = id
        self.level = level

id, level = input().split()

raw = User()
new = User(id, level)


print(f"user {raw.id} lv {raw.level}")
print(f"user {new.id} lv {new.level}")