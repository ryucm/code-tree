class Human():
    def __init__(self, name="", score=100):
        self.name=name
        self.score=score

human_list = []
for i in range(5):
    name, score = input().split()
    human_list.append(Human(name, int(score)))

result = Human()
for h in human_list:
    if h.score < result.score:
        result = h

print(result.name, result.score)