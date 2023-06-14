# This program calculates the percentage tip we want to give, based on the total bill.
# It also split the value with the people at the table.
#

print("\n\nWelcome to Tip Calculator")
print("======= == === ==========\n")

total_bill = float(input("What's the total bill? $"))
percent_tip = int(input("What's the percentage tip would you like to give? 10%, 12% or 15%: "))
total_people = int(input("How many people to split the bill with: "))

total = round((total_bill+(total_bill*percent_tip/100))/total_people, 2)

print(f"\nEach person should pay ${total}")

