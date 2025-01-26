weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))

# Calculate BMI
BMI = (weight / (height * height)) * 703
print(BMI)
# Determine the category
if BMI < 19:
    print("You are underweight.")
elif BMI >= 19 and BMI <= 25:
    print("You are fine.")
elif BMI > 25 and BMI <= 30:
    print("You are overweight.")
else:  # BMI > 30
    print("You are in the obese category. Consider consulting a healthcare provider.")
