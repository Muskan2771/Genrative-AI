# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


num=int(input("Enter number of passengers: "))
ticket_cost=int(input("Enter ticket per cost: "))
total_amt=0

for i in range(1,num+1):
    print("Passenger ",i)
    age=int(input("Enter the age of passenger: "))
    if age<12:
        final_amt=ticket_cost*0.70
    elif age>59:
        final_amt=ticket_cost*0.50
    else:
        final_amt=ticket_cost

    total_amt=total_amt+final_amt      

print("Total you have to pay: ",total_amt)           