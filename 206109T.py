def calculate_bmi(weight, height, is_imperial=False):
    if is_imperial:
        # Convert weight from pounds to kilograms and height from inches to meters
        weight = weight * 0.453592
        height = height * 0.0254
    return weight / (height ** 2)

def interpret_bmi(bmi, gender):
    if gender == "Male":
        if bmi < 18.5:
            return "Underweight", "You may need to gain some weight."
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight", "You are in a healthy weight range."
        elif 25 <= bmi < 29.9:
            return "Overweight", "You may consider losing some weight for better health."
        else:
            return "Obese", "You should consult a healthcare professional for weight management."
    elif gender == "Female":
        # Adjust BMI categories and recommendations for females as needed
        # Define your own thresholds and recommendations here
        pass
    else:
        return "N/A", "BMI categories vary by gender."

def calculate_ideal_weight_range(height, is_imperial=False):
    if is_imperial:
        height = height * 0.0254
    lower_bound = 18.5 * (height ** 2)
    upper_bound = 24.9 * (height ** 2)
    return lower_bound, upper_bound

print("Welcome to the BMI Calculator!")
print("-------------------------------")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female/Other): ").strip().title()
weight_unit = input("Enter the unit for weight (Kilograms/Pounds): ").strip().title()
height_unit = input("Enter the unit for height (Meters/Inches): ").strip().title()
weight = float(input(f"Enter your weight in {weight_unit}: "))
height = float(input(f"Enter your height in {height_unit}: "))

is_imperial = weight_unit == "Pounds" and height_unit == "Inches"
bmi = calculate_bmi(weight, height, is_imperial)
bmi_category, bmi_recommendation = interpret_bmi(bmi, gender)
ideal_weight_range = calculate_ideal_weight_range(height, is_imperial)

print("\nCalculating your BMI and Ideal Weight Range...")
print("-------------------------------")

print(f"{name}, aged {age}, your BMI is: {bmi:.2f}")
print(f"You are in the '{bmi_category}' category. {bmi_recommendation}")
print(f"The ideal weight range for your height is between {ideal_weight_range[0]:.2f} {weight_unit} and {ideal_weight_range[1]:.2f} {weight_unit}.")
print("-------------------------------")

if bmi_category == "Underweight":
    print("You are underweight. Consider consulting a healthcare professional.")
elif bmi_category == "Overweight" or bmi_category == "Obese":
    print("You are in an unhealthy BMI category. Consult a healthcare professional for guidance.")
else:
    print("You are within the healthy BMI range. Keep up the good work!")

print("Thank you for using the BMI Calculator. Stay healthy!")
