from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, persons):
        self.persons=persons

    @abstractmethod
    def calculate_toll(self):
        pass

class TwoWheeler(Vehicle):
    def calculate_toll(self):
        toll=20
        if self.persons>2:
            extra = (self.persons-2)*10
            toll = toll+extra
        return toll

class ThreeWheeler(Vehicle):
    def calculate_toll(self):
        toll=30
        if self.persons>3:
            extra = (self.persons-3)*20
            toll = toll+extra
        return toll

class FourWheeler(Vehicle):
    def calculate_toll(self):
        toll = 40
        if self.persons>4:
            extra = (self.persons-4)*40
            toll = toll+extra
        return toll

class HeavyVehicle(Vehicle):
    def calculate_toll(self):
        toll = 60
        if self.persons>6:
            extra = (self.persons - 6)*100
            toll = toll+extra
        return toll

while True:
    print("\n----- Toll Menu -----")
    print("1.Two Wheeler")
    print("2.Three Wheeler")
    print("3.Four Wheeler")
    print("4.Heavy Vehicle")
    print("5.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Thank you! Visit again.")
        break

    persons = int(input("Enter number of persons: "))

    if choice == 1:
        v = TwoWheeler(persons)
    elif choice == 2:
        v = ThreeWheeler(persons)
    elif choice == 3:
        v = FourWheeler(persons)
    elif choice == 4:
        v = HeavyVehicle(persons)
    else:
        print("Invalid choice")
        continue

    print("Total Toll Amount = Rs.", v.calculate_toll())
