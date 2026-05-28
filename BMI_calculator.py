weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height * height)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You are Normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")
