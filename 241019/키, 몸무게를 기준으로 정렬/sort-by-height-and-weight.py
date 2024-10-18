class Person():
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

n = int(input())
people = []

for i in range(n):
    name, tall, weight = input().split()
    people.append(Person(name, int(tall), int(weight)))

people.sort(key=lambda x: (x.tall, -x.weight))

for i in people:
    print(f"{i.name} {i.tall} {i.weight}")