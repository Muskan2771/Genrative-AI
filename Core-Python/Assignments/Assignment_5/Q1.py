#Write a program to prompt user to enter userid and password. If Id and 
#password is incorrect give him chance to re-enter the credentials. Let him try 3 
#times. After that program to terminate.

userid = "123456"
password = "Muskan"

attempts = 3

while attempts > 0:
    u_id = input("Enter the userid: ")
    pass_word = input("Enter the password: ")

    if u_id == userid and pass_word == password:
        print("You are successfully Logged in")
        break
    else:
        attempts -= 1
        print("Wrong userid or password")

        if attempts > 0:
            print("Please try again. Attempts left:", attempts)
        else:
            print("Your 3 attempts are over. Access Denied!")
