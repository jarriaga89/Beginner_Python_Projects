import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Josh's Random Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

baseletter = random.choice(letters)
basesymbol = random.choice(symbols)
basenumber = random.choice(numbers)

for chosenletters in range(nr_letters - 1):
  baseletter = (baseletter + random.choice(letters))

for chosensymbols in range(nr_symbols - 1):
  basesymbol = (basesymbol + random.choice(symbols))

for chosennumbers in range(nr_numbers - 1):
  basenumber = (basenumber + random.choice(numbers))  

finaleasypass = baseletter + basesymbol + basenumber
hardpass = random.sample(finaleasypass, (len(finaleasypass))) 
stringhardpass = "".join(hardpass)
print(f"Your random password is '{stringhardpass}'.")
