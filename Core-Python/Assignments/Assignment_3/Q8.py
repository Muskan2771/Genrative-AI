# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random
print("Enter Userid and Password")

user_id=input("Enter userid: ")
pass_word=input("Enter the password: ")

if user_id=="123456" and pass_word=="Muskan":
            OTP=random.randint(1000,9999)
            print(OTP)
            otp=int(input("Enter the OTP: "))
            if OTP==otp:      
                print("Your have successfuly logged in")
            else: 
                    print("Falied Incorrect OTP")    
else:  
        print("Enter correct Userid and Password")    
                