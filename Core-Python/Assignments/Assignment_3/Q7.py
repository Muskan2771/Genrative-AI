#Write a program to check if user has entered correct userid and password.

print("Enter Userid and Password")

user_id=int(input("Enter userid: "))
pass_word=input("Enter the password: ")
if user_id==123456 and pass_word=="Muskan":
            print("Your successfuly logged in")
else:
        print("Enter correct Userid and Password")            