weight = float(input("\n\nYour weight in kg: "))

height = float(input("Your height in m: "))

bmi = weight/(height**2)

print(f"\nYour BMI is {round(bmi, 2)}")

if bmi <= 18.4:
    print("You're under weight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You're normal weight")
elif bmi >= 25 and bmi <= 39.9:
    print("You're overweight")
else:
    print("You're obese")


