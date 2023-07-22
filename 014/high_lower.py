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


'''
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'

'''

name1 = choice(data)
name2 = pick_new(name1)

'''
score = 0


print("Your current score: {score}")
'''


print(f"Compare A: {name1['name']}, {name1['description']}, {name1['country']}.")

print('\nVs\n')

print(f"Abainst B: {name2['name']}, {name2['description']}, {name2['country']}.")


followers = input("\n\nWho has more followers? Type A or B: ").lower()




