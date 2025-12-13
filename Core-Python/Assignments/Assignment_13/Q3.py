data = {1:"Muskan", 2:"Saniya", 3:"Rehan", 4:"Asha"}

roll_no = int(input("Enter roll number: "))

if roll_no in data:
    print("Roll number exists")
else:
    print("Roll number does not exist")
