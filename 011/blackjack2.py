#
# Blackjack
#
# This version doesn't consider the total
# amount of cards in a real deck. Thus,
# it won't delete the cards as they're
# drawn from the deck.
#

from random import choice

# The ace counts 11 unless the total sum
# more than 21, in this case it sums 1.
#
# jack, queen and king cards count as 10.
#


# sum the the amount of points
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


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = []
pc = []

# pick 2 random numbers for both players
for x in range(2):
    user.append(choice(cards))
    pc.append(choice(cards))

#
if user[1] == 11 and points(user) > 21:
    user[1] = 1

if pc[1] == 11 and points(pc) > 21:
    pc[1] = 1


while points(user) < 21 or points(pc) < 21:
    print(f"\nYour cards: {user}")
    print(f"Compiter's first card: [{pc[0]}]\n")

    # Check winner
    if check_winner(user) or points(pc) > 21:
       print("\nYou win!\n")
       break
    elif check_winner(pc) or points(user) > 21:
       print("\nYou lose!\n")
       break

    another = input("\nType Y to get another card or N to pass: ").lower()

# give the player or the pc a new card
    if another == 'y':
        card = choice(cards)
        if card == 11 and points(user)+card > 21:
            card = 1
        user.append(card)
    else:
        card = choice(cards)
        if card == 11 and points(pc)+card > 21:
            card = 1
        pc.append(card)


