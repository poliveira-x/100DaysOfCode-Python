# life in weeks counts the amount of weeks one will liv
# from today untill reach the age of 90.
#

current_age = int(input("\n\nHow old are you: "))

years_left = 90-current_age
days_left = years_left*365
months_left = years_left*12
weeks_left = int(days_left/7)

print(f"\nYears {years_left}")
print(f"Months {months_left}")
print(f"Weeks {weeks_left}")
print(f"Days {days_left}\n")






