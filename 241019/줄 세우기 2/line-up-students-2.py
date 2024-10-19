class Student():
    def __init__(self, tall, weight, num):
        self.tall = tall
        self.weight = weight
        self.num = num
    
N = int(input())
result = []

for i in range(N):
    tall, weight = tuple(map(int, input().split()))
    result.append(Student(tall, weight, i+1))

result.sort(key = lambda x: (x.tall, -x.weight))

for i in result:
    print(f"{i.tall} {i.weight} {i.num}")