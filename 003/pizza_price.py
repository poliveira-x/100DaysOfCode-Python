# Calculates the final price of a pizza deppending on its size
# and what we want to add to it
#

size = input("\n\nWhat's the size? S (small), M(medium) or L(large): ").upper()
pepperoni = input("Would you like to add pepperoni? Y/N: ").upper()
cheese = input("Would you like to add cheese? Y/N: ").upper()

if size == "S":
    price = 15.0
elif size == "M":
    price = 20.0
elif size == "L":
    price = 25.0

if pepperoni == "Y" and price == 15.0:
    price += 1
elif pepperoni == "Y" and price > 15.0:
    price += 2 

if cheese == "Y":
    price += 1

print(f"\nTotal $ {price}")

