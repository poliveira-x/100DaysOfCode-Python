#
import subprocess
bidders = {}
sn = 's'

while sn == 's':
    name = input("\nWhat's your name: ")
    bid = float(input("Your bid: "))
    sn = input("\nAnother bid S/N: ")[0].lower()

    # this line works only
    # on linux like systems
    subprocess.run(["clear"])

    bidders[name] = bid

g_bidder = ''
g_bid = 0
for i in bidders:
    if bidders[i] > g_bid:
        g_bidder = i
        g_bid = bidders[i]

print(f"\nThe highest bidder is {g_bidder} with a bid of {g_bid}")

