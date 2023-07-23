#
# High lower game.
# We chose a name. We keep playing or lose depending whether we
# pick the right option
#

from game_data import data
from random import choice
from os import system

# pick an item
def pick_new(item1):
    item2 = choice(data)
    if item1 == item2:
        while item1 == item2:
            item2 = choice(data)
    return item2


name1 = choice(data)
score = 0

while True:
    system('clear') # clear works only on unix-like systems
    print("High Lower Game")
    print("==== ===== ====\n")
    name2 = pick_new(name1)

    print(f"Compare A: {name1['name']}, {name1['description']}, {name1['country']}.")
    print('\nVs\n')
    print(f"Abainst B: {name2['name']}, {name2['description']}, {name2['country']}.")

    followers = input("\n\nWho has more followers? Type A or B: ").lower()

    if followers == 'a':
        if name1['follower_count'] > name2['follower_count']:
            score += 1
            name1 = name2.copy()
        else:
            break
    elif followers == 'b':
        if name2['follower_count'] > name1['follower_count']:
            score += 1
            name1 = name2.copy()
        else:
            break

print(f"\n\nYou lose!\nYour score: {score}")



