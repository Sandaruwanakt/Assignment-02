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


while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            continue

        bmi = calculate_bmi(weight, height)
        bmi_category = interpret_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are in the '{bmi_category}' category.")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

    another_calculation = input("Do you want to calculate another BMI (yes/no)? ").lower()
    if another_calculation != "yes":
        break
