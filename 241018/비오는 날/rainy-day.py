class Weather():
    def __init__(self, date='9999-12-31', week=None, weather=None):
        self.date = date
        self.week = week
        self.weather = weather

n = int(input())

arr = []
for i in range(n):
    date, week, weather = input().split()
    arr.append(Weather(date, week, weather))

result = Weather()

for i in range(len(arr)):
    if result and arr[i].weather == 'Rain' and result.date > arr[i].date:
        result = arr[i]

print(f"{result.date} {result.week} {result.weather}")