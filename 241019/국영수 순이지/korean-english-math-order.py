class Student():
    def __init__(self, name, korean, english, math):
        self.name= name
        self.korean = korean
        self.english = english
        self.math = math
    
n = int(input())
people = []

for i in range(n):
    name, korean, english, math = input().split()
    people.append(Student(name, int(korean), int(english), int(math)))

people.sort(key = lambda x: (-x.korean, -x.english, -x.math))

for i in people:
    print(f"{i.name} {i.korean} {i.english} {i.math}")