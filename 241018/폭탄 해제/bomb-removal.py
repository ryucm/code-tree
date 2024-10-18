class Bomb():
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = input().split()
bomb = Bomb(code, color, sec)

print(f"code : {bomb.code}")
print(f"color : {bomb.color}")
print(f"second : {bomb.sec}")