from Q1 import Student

class EnggStudent(Student):
    def __init__(self, student_id=0, name="", age=0, perc=0.0, branch="", internal_marks=0):
        super().__init__(student_id, name, age, perc)
        self.branch = branch
        self.internal_marks = internal_marks

    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internal_marks = int(input("Enter Internal Marks: "))

    def display(self):
        super().display()
        print("Branch:", self.branch)
        print("Internal Marks:", self.internal_marks)

    def calculate_rank(self):
        total = (self.percentage * 0.7) + (self.internal_marks * 0.3)
        return "Excellent" if total >= 70 else "Average"

    def __str__(self):
        return f"EnggStudent[Name={self.name}, Branch={self.branch}, Rank={self.calculate_rank()}]"
