# password based on the given data.
#

# Generates a list with the alphabet
# upper and lower case
letters = []
n_letters = []
for i in range(65, 65+26):
    letters.append(chr(i))

for i in letters:
    n_letters.append(i.lower())

for i in n_letters:
    letters.append(i)

numbers = []
for i in range(0, 10):
    numbers.append(str(i))

symbols = ["@", "#", "&", "*", "-","+", "-", "+", "=", "$", "/", "%", "?", "!"]


print(letters, numbers, symbols)



