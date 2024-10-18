class Human():
    def __init__(self, name, score):
        self.name=name
        self.score=score

result = []
for i in range(5):
    name, score = input().split()
    result.append(Human(name, score))

print(result[0].name, result[0].score)