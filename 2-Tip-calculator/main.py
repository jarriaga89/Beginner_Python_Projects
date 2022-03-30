print("Welcome Josh's split bill calculator. With this tool you can easily tell how much each one will have to pay.")
total_bill = float(input("What was the total bill? $"))

percent_options = int(input("Want to add a tip? If so, how much (0 for none)? $"))
percent_toadd = ((total_bill / 100) * percent_options)

total_people = int(input("How many people are sharing the bill? "))
split_ammount = ((total_bill + percent_toadd) / total_people)

splitrounded = round(split_ammount, 2)
tosplit = f"Each person should pay: ${splitrounded}"
print(tosplit)