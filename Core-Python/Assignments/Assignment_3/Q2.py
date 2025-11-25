#Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet=input("Enter any alphabet: ")

ch = alphabet.upper()
if ch=="A"  or  ch=="I" or ch=="E"  or ch=="O"  or ch=="U" :
       print(alphabet,"This is vowel.")
else:
       print(alphabet,"This is consonant.")       