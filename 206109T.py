# Function to calculate BMI
def calculate_bmi(weight, height):
    # Formula for BMI: weight (kg) / (height (m) * height (m))
    return weight / (height ** 2)


# Function to interpret BMI value
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# Main program
if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Interpret BMI
        bmi_category = interpret_bmi(bmi)

        # Display the result
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are in the '{bmi_category}' category.")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
