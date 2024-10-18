class Student():
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
people = []

for i in range(n):
    name, kor, eng, math = input().split()
    people.append(Student(name, int(kor), int(eng), int(math)))

people.sort(key=lambda x: (x.kor + x.eng + x.math))

for i in people:
    print(f"{i.name} {i.kor} {i.eng} {i.math}")