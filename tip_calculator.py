print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_percent = tip / 100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
total_bill_person = total_bill / people
# total_bill_round = round(total_bill_person, 2)
total_bill_round ="{:.2f}".format(total_bill_person)
print(f"Each person should pay: ${total_bill_round}")
