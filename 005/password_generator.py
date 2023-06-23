# password generator
#

from random import choice, randint

letters = ""
passw = []
password = ""

for i in range(65, 65+26):
    letters += chr(i)

for i in range(97, 97+26):
    letters += chr(i)

numbers = ""
for i in range(0, 10):
    numbers += str(i)

symbols = "!@#$%&*_-+={}[]?/<>" 


qtd_l = int(input("How many leters? "))
qtd_n = int(input("How many numbers? "))
qtd_s = int(input("How many symbols? "))

for i in range(qtd_l):
    passw.append( choice(letters))

for i in range(qtd_n):
    passw.append(choice(numbers))

for i in range(qtd_s):
    passw.append(choice(symbols))

for i in range(len(passw)):
    l = choice(passw)
    password += l
    passw.remove(l)


print(f"\n\tPassword => {password}\n")


