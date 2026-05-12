import random 
import string 

length = int(input( "Enter password length: "))
use_letters = ( input ( "Include letter? (Yes/no):"))
use_numbers = (input ("Include numbers? (Yes/no): "))
use_symbols = ( input (" Include symbols? (Yes/no): ")).lower()
characters = ""

if characters == "":
    print(" Choose at least one option.")







if use_letters == "Yes":
    characters += string.ascii_letters

if use_numbers == "Yes": 
    characters += string.digits 

if use_symbols == "Yes": 
    characters += string.punctuation

else: 
    password = ""    

for i in range(length): 
    password += random .choice(characters)
 

    strength = ""

if len(password) < 8:
    strength = "weak"  

elif len(password) <= 12:
    strength = " Mid"

else: 
     strength = "Good"
    

print("\nGenerated Password:")
print(password)
