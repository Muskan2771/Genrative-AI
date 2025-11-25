#Convert the time entered in hh,min and sec into seconds.

hour=int(input("Enter the hours: "))
mintue=int(input("Enter the mintue: "))
second=int(input("Enter the second: "))

sec=(hour * 3600) + (mintue * 60) + second

print("Time in seconds: ",sec,"sec")