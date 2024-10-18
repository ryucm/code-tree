class Student():
    def __init__(self, tall, weight, number):
        self.tall = tall
        self.weight = weight
        self.number = number

n = int(input())
people = []

for i in range(1, n+1):
    tall, weight = input().split()
    people.append(Student(int(tall), int(weight), i))

people.sort(key=lambda x: (-x.tall, -x.weight, x.number))

for i in people:
    print(f"{i.tall} {i.weight} {i.number}")