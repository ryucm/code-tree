class Person():
    def __init__(self, name, num, location):
        self.name = name
        self.num = num
        self.location = location

n = int(input())

person_list = []
name_list = []
for i in range(n):
    name, num, location = input().split()
    person_list.append(Person(name, num, location))
    name_list.append(name)

name_list.sort(reverse=True)

for i in person_list:
    if name_list[0] == i.name:
        print(f"name {i.name}")
        print(f"addr {i.num}")
        print(f"city {i.location}")
        break