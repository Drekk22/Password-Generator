import random 
import string 

length = int(input( "Enter password length: "))

character = string.ascii_letters  + string.digits +  string.punctuation

password = ""

for i in range(length): 
    password += random .choice(character)

    print("\nGenerated Password:")
    print(password)