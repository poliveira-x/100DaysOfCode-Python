# hangman
#
from random import choice
word_list = ["apple", "chocolate", "avocado"]
lives = 6
win = "You win!!!"

# pick a random word
word = choice(word_list)

# generate the blanks
blanks = []
for i in range(len(word)):
    blanks.append("_")

while (lives>0) and ("_" in blanks):
    print(f"\n{blanks}")

    # get an user guess
    guess = input("Guess a letter: ")[0].lower()

    # the letter exists
    if guess in word:
        for i in range(len(word)):
            # replace blanks
            if word[i] == guess:
                blanks[i] = guess
    else:
        # take a life
        lives -= 1
        if lives == 0:
            win = "You lose !!!"


print(f"\n\n{win}\n")

