# input 150, 12, 5

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

num_of_splits = int(input("How many people to split the bill? "))

bill_with_tip = total_bill * (1 + tip_percentage / 100)

individual_bill = bill_with_tip / num_of_splits

# print(f"Each person should pay: ${round(individual_bill, 2)}")
# print(f"Each person should pay: ${format(individual_bill, '.2f')}")

print(f"Each person should pay: ${individual_bill:.2f}")