#Write a program to convert days into years, weeks and days.

data=int(input("Enter the total days: "))

year=data//365
remaining_days=data%365

week=remaining_days//7
day=remaining_days%7

print("YEAR:",year)
print("WEEK:",week)
print("DAYS:",day)



