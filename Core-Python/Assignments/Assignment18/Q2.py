class Distance:
    def __init__(self,km=0,m=0,cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        self.normalize()

    def normalize(self):
        self.m += self.cm // 100
        self.cm = self.cm % 100

        self.km += self.m // 1000
        self.m = self.m % 1000

    def __del__(self):
        print("Distance object destroyed")

    def __add__(self, other):
        return Distance(self.km + other.km,
                        self.m + other.m,
                        self.cm + other.cm)

    def __sub__(self, other):
        return Distance(self.km - other.km,
                        self.m - other.m,
                        self.cm - other.cm)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

d1 = Distance(2,500,75)
d2 = Distance(1,750,50)

print("Addition:", d1 + d2)
print("Subtraction:", d1 - d2)
