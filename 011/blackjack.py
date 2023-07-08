#
# Blackjack
#

from random import choice

# sum the the total of points
def points(lst):
    total = 0
    for i in lst:
        total += i
    return total


# Check whether someone won
def check_winner(player):
    if points(player) == 21:
        return True
    else:
        return False


#
# 52 integers that representing the cards
# of a deck the ace, jack, queen and king
# are represented as numbers. 4 repeated
# numbers to represent the 4 different
# suit of cards in a deck
#
cards = [11, 11, 11, 11, # aces 
         2, 2, 2, 2, 
         3, 3, 3, 3, 
         4, 4, 4, 4, 
         5, 5, 5, 5, 
         6, 6, 6, 6, 
         7, 7, 7, 7, 
         8, 8, 8, 8, 
         9, 9, 9, 9, 
         10, 10, 10, 10, 
         10, 10, 10, 10, # jacks
         10, 10, 10, 10, # queens
         10, 10, 10, 10] # kings

user = []
pc = []

# pick 2 random cards for both players
# and delete them from the deck
for x in range(2):
    card = choice(cards)
    user.append(card)
    cards.remove(card)

    card = choice(cards)
    pc.append(choice(cards))
    cards.remove(card)

# The ace counts 11 unless the total sum
# goes over 21, in this case the last
# drawn ace counts 1.
if user[1] == 11 and points(user) > 21:
    user[1] = 1

if pc[1] == 11 and points(pc) > 21:
    pc[1] = 1


while points(user) < 21 or points(pc) < 21:
    print(f"\nYour cards: {user}")
    print(f"Computer's first card: [{pc[0]}]\n")

# Check winner
    if check_winner(user) or points(pc) > 21:
       print("\nYou win!\n")
       break
    elif check_winner(pc) or points(user) > 21:
       print("\nYou lose!\n")
       break

    another = input("\nType Y to get another card or N to pass: ").lower()

# give the user or the pc a new card
    if another == 'y':
        card = choice(cards)
        cards.remove(card)
        if card == 11 and points(user)+card > 21:
            card = 1
        user.append(card)
    else:
        card = choice(cards)
        cards.remove(card)
        if card == 11 and points(pc)+card > 21:
            card = 1
        pc.append(card)


