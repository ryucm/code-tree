class Person():
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

people = []

for i in range(5):
    name, tall, weight = input().split()
    people.append(Person(name, int(tall), float(weight)))

people.sort(key=lambda x: (x.name))

print("name")
for i in people:
    print(f"{i.name} {i.tall} {i.weight}")
print("")
print("height")
people.sort(key=lambda x: (-x.tall))
for i in people:
    print(f"{i.name} {i.tall} {i.weight}")