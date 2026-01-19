from SYMarks import SYMarks
from TYMarks import TYMarks


class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks      # Containment
        self.ty_marks = ty_marks      # Containment

    def calculate_result(self):
        total_computer_marks = (
            self.sy_marks.computer_total +
            self.ty_marks.theory +
            self.ty_marks.practical
        )

        percentage = total_computer_marks / 3

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("----- Student Result -----")
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"SY Computer Marks : {self.sy_marks.computer_total}")
        print(f"TY Theory Marks   : {self.ty_marks.theory}")
        print(f"TY Practical Marks: {self.ty_marks.practical}")
        print(f"Percentage        : {percentage:.2f}")
        print(f"Grade             : {grade}")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    sy = SYMarks(65, 70, 60)
    ty = TYMarks(68, 72)

    student = Student(101, "Muskan Shaikh", sy, ty)
    student.calculate_result()
