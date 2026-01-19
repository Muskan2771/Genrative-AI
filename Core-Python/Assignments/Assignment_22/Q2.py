import pickle
import os

from Q1 import Emp  
FILENAME = "emp.dat"

# ---------- ADD RECORD ----------
def add_record():
    emp_list = []

    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            emp_list = pickle.load(f)

    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    emp_list.append(Emp(eid, ename, basic))

    with open(FILENAME, "wb") as f:
        pickle.dump(emp_list, f)

    print("Record Added Successfully")


# ---------- SEARCH RECORD ----------
def search_record():
    eid = int(input("Enter Employee ID to search: "))

    if not os.path.exists(FILENAME):
        print("File not found")
        return

    with open(FILENAME, "rb") as f:
        emp_list = pickle.load(f)

    for emp in emp_list:
        if emp.eid == eid:
            emp.display()
            return

    print("Record Not Found")


# ---------- DELETE RECORD ----------
def delete_record():
    eid = int(input("Enter Employee ID to delete: "))

    if not os.path.exists(FILENAME):
        print("File not found")
        return

    with open(FILENAME, "rb") as f:
        emp_list = pickle.load(f)

    emp_list = [emp for emp in emp_list if emp.eid != eid]

    with open(FILENAME, "wb") as f:
        pickle.dump(emp_list, f)

    print("Record Deleted")


# ---------- EDIT RECORD ----------
def edit_record():
    eid = int(input("Enter Employee ID to edit: "))

    if not os.path.exists(FILENAME):
        print("File not found")
        return

    with open(FILENAME, "rb") as f:
        emp_list = pickle.load(f)

    for emp in emp_list:
        if emp.eid == eid:
            emp.ename = input("Enter New Name: ")
            emp.basic = float(input("Enter New Basic Salary: "))
            print("Record Updated")
            break
    else:
        print("Record Not Found")

    with open(FILENAME, "wb") as f:
        pickle.dump(emp_list, f)


# ---------- DISPLAY ALL ----------
def display_all():
    if not os.path.exists(FILENAME):
        print("No records found")
        return

    with open(FILENAME, "rb") as f:
        emp_list = pickle.load(f)

    print("\n--- Employee Records ---")
    for emp in emp_list:
        emp.display()


# ---------- MAIN ----------
def main():
    while True:
        print("\n--- MENU ---")
        print("1. Add Record")
        print("2. Search Record")
        print("3. Delete Record")
        print("4. Edit Record")
        print("5. Display All Records")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_record()
        elif choice == 2:
            search_record()
        elif choice == 3:
            delete_record()
        elif choice == 4:
            edit_record()
        elif choice == 5:
            display_all()
        elif choice == 6:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
