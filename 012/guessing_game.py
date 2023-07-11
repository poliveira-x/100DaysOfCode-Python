#
# Guessing game
#

from random import randint

number = randint(1,100)

print("\n  Welcome to the number guessing game!")
print('='*45,'\n')

print("I'm thinking of a number between 1 and 100\n")

level = input("Choose a difficulty level 'easy' or 'hard': ").lower()

if level == 'easy':
    guesses = 10
elif level == 'hard':
    guesses = 5
else:
    print("\nOption does not exist!\n")

for i in range(guesses):
    print(f"\nYou have {guesses-i} attempts remaining.\n")

    guess = int(input("Guess a number: "))

    if guess == number:
        print(f"\nYOU GOT IT! The number was {number}\n")
        break
    elif guess > number:
        print("\nToo high.\n")
    elif guess < number:
        print("\Too low.\n")

if guesses == 0 or guess != number:
    print("\nYOU LOSE!\n")

