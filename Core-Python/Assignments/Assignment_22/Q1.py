class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print("Employee ID   :", self.eid)
        print("Employee Name :", self.ename)
        print("Basic Salary  :", self.basic)
