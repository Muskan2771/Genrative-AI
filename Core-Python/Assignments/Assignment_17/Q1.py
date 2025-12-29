class Student:
    def __init__(self,student_id=0,name="",age=0,perc=0.0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = perc

    def accept(self):
        self.student_id = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)

    def calculate_rank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        else:
            return "Fail"

    def __str__(self):
        return f"Student[ID={self.student_id}, Name={self.name}, Rank={self.calculate_rank()}]"
