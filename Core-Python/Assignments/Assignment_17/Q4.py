class College:
    def __init__(self,capacity):
        self.capacity = capacity
        self.students = []

    def add_student(self,student):
        if len(self.students) < self.capacity:
            self.students.append(student)
        else:
            print("College capacity full")

    def get_student(self,student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def remove_student(self,student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("Student removed")
                return
        print("Student not found")

    def __str__(self):
        result = "College Students:\n"
        for s in self.students:
            result += str(s) + "\n"
        return result
