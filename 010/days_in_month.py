#
# This program return the amount of days in a given month.
# It tests if the year is leap to return the number of days in february.
#

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap_year(year) == True and month == 2:
        return 29
    else:
        return month_days[month+1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

leap = ""
if leap_year(year) == True:
    leap = "a leap year"
else:
    leap = "not a leap year"


print (f"\nThe year {year} is {leap} and the month {month} has {days_in_month(year, month)} days.\n")


