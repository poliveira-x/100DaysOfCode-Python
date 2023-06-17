# password based on the given data.
#

from random import choice, randint

letters = ""
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
i

lett = []
for i in range(qtd_l):
    lett.append( choice(letters))

numb = []
for i in range(qtd_n):
    numb.append(choice(numbers))

symb = []
for i in range(qtd_s):
    symb.append(choice(symbols))

password_l=[]
for i in range(qtd_l+qtd_n+qtd_s):
    if len(lett) > 0:
        x = randint(0, len(lett)-1)
        password_l.append(lett[x])
        lett.remove(lett[x])

    if len(numb) > 0:
        x = randint(0, len(numb)-1)
        password_l.append(numb[x])
        numb.remove(numb[x])

    if len(symb) > 0:
        x = randint(0, len(symb)-1)
        password_l.append(symb[x])
        symb.remove(symb[x])

password = ""
for i in range(len(password_l)):
    l = choice(password_l)
    password += l
    password_l.remove(l)

print(f"\n\tPassword => {password}\n")


