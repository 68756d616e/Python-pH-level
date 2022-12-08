# PH level calculator 

import random

print("Please inform me of the PH number from 0 to 14")
ph = int(input("What is the number of the PH level? : "))

# ph_acidic = 6
# ph_neutral = 7
# ph_alkaline = 14

if ph <= 6:
    print(f"The PH level for {ph} is acidic")
elif ph == 7:
        print(f"The PH for {ph} is neutral")
elif ph > 7:
    print(f"The PH for {ph} is alkaline")

fact = input("Would you like to know a fact? press Y or N :")

facts = ["0 - 6 is acidic", "7 is neutral", "8 - 14 is alkaline"]

if fact == "Y" or fact == "y":
    print(f"Here is your random fact: {random.choice(facts)}") 
elif fact == "N" or fact == "n":
    print("Ok, have a nice day")
else:
    print("I dont understand, chow!")
