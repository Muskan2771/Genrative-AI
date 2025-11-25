#Write a program to calculate profit or loss.

sp=float(input("Enter the Selling Price: "))
cp=float(input("Enter the Cost Price: "))

if sp>cp:
    profit=sp-cp
    print("You gain",profit,"Profit")
elif cp>sp:
    loss=cp-sp
    print("You lost",loss,"Loss")    
else:
    print("No profit and No loss")    