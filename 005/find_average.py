# This program finds the average
# of a set of numbers given by the use
#

numbers = input("\n\nType a set of numbers: ").split(" ")

# converte a lista de string para int
x = 0
for i in numbers:
    numbers[x] = int(i)
    x+=1

total = 0
for i in numbers:
    total += i

print(total/len(numbers))


