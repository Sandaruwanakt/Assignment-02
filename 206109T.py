def calculate_bmi(weight, height):
    return weight / (height ** 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

print("Welcome to the BMI Calculator!")
print("-------------------------------")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
bmi_category = interpret_bmi(bmi)

print("\nCalculating your BMI...")
print("-------------------------------")

print(f"{name}, aged {age}, your BMI is: {bmi:.2f}")
print(f"You are in the '{bmi_category}' category.")
print("-------------------------------")

if bmi < 18.5:
    print("You are underweight. Consider consulting a healthcare professional.")
elif bmi >= 25:
    print("You are overweight. Consider maintaining a balanced diet and staying physically active.")
else:
    print("You are within the healthy BMI range. Keep up the good work!")

print("Thank you for using the BMI Calculator. Stay healthy!")

