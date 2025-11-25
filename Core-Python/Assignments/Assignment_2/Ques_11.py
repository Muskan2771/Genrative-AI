# Write a program to accept an integer amount from user and 
# tell minimum number of notes needed for representing that amount.

amt=int(input("Enter the Amount:"))

Notes_500=amt//500
amt=amt%500

Notes_200=amt//200
amt=amt%200

Notes_100=amt//100
amt=amt%100

Notes_50=amt//50
amt=amt%50

Notes_20=amt//20
amt=amt%20

Notes_10=amt//10
amt=amt%10

print("500 Notes:", Notes_500)
print("200 Notes:", Notes_200)
print("100 Notes:", Notes_100)
print("50 Notes:", Notes_50)
print("20 Notes:", Notes_20)
print("10 Notes:", Notes_10)


