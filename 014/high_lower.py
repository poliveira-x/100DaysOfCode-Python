#
#
#

from game_data import data
from random import choice

# pick an item
def pick_new(item1):
    item2 = choice(data)
    if item1 == item2:
        while item1 == item2:
            item2 = choice(data)
    return item2


name1 = choice(data)
name2 = pick_new(name1)

score = 0


print("Your current score: {score}")

print(f"Compare A: {name1}")

print(f"Against B: {name2}")

print("Who has more followers? Type A or B: ")



