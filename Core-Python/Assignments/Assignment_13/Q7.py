data = {1:"Muskan", 2:"Saniya", 3:"Rehan", 4:"Asha"}

roll_no = int(input("Enter roll number to remove: "))

if roll_no in data:
    del data[roll_no]

print(data)
