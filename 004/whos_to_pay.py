# select a random name from a given list
#

from random import randint

names = input("\nType the names: ").split(" ")

c_name = randint(0,len(names)-1)

print(f"\n{names[c_name]} is the chosen to pay the check.")


