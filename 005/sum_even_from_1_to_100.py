# Sum all the even numbers from
# 1 to 100 including bot
#

total = 0
for i in range(1, 101):
    if i%2 == 0:
        total += i

print(f"\nThe sum of all the even numbers from 1 to 100 is {total}")
    
