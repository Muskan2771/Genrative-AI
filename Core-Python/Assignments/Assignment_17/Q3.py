from Q1 import Student

class MedicalStudent(Student):
    def __init__(self,student_id=0,name="",age=0,perc=0.0,specialization="",internship_marks=0):
        super().__init__(student_id,name,age,perc)
        self.specialization = specialization
        self.internship_marks = internship_marks

    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.internship_marks = int(input("Enter Internship Marks: "))

    def display(self):
        super().display()
        print("Specialization:", self.specialization)
        print("Internship Marks:", self.internship_marks)

    def calculate_rank(self):
        if self.internship_marks >= 80:
            return "Top Performer"
        elif self.internship_marks >= 60:
            return "Good"
        else:
            return "Needs Improvement"

    def __str__(self):
        return f"MedicalStudent[Name={self.name}, Specialization={self.specialization}, Rank={self.calculate_rank()}]"
