class Place():
    def __init__(self, secret_code, place, time):
        self.secret_code = secret_code
        self.place = place
        self.time = time

secret_code, place, time = input().split()
a = Place(secret_code, place, time)

print(f"secret code : {a.secret_code}")
print(f"meeting point : {a.place}")
print(f"time : {a.time}")