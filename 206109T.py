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

def calculate_ideal_weight_range(height):
    lower_bound = 18.5 * (height ** 2)
    upper_bound = 24.9 * (height ** 2)
    return lower_bound, upper_bound

def suggest_weight_goal(current_weight, ideal_weight_range):
    lower_bound, upper_bound = ideal_weight_range
    if current_weight < lower_bound:
        return "You are under your ideal weight range. Consider gaining weight."
    elif current_weight > upper_bound:
        return "You are above your ideal weight range. Consider losing weight."
    else:
        return "You are within your ideal weight range. Maintain your current weight."

def suggest_caloric_intake(bmi_category):
    if bmi_category == "Underweight":
        return "You may need to increase your caloric intake."
    elif bmi_category == "Overweight":
        return "You may need to reduce your caloric intake."
    else:
        return "Maintain a balanced diet to stay in the healthy BMI range."

print("Welcome to the Enhanced BMI Calculator!")
print("-------------------------------")

name = input("Enter your name: ")
gender = input("Enter your gender (Male/Female): ").strip().title()
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))  # Fixed missing parenthesis here

bmi = calculate_bmi(weight, height)
bmi_category = interpret_bmi(bmi)
ideal_weight_range = calculate_ideal_weight_range(height)
weight_goal = suggest_weight_goal(weight, ideal_weight_range)
caloric_intake_suggestion = suggest_caloric_intake(bmi_category)

# Determine the appropriate title based on gender
if gender == "Male":
    title = "Mr."
elif gender == "Female":
    title = "Mrs."
else:
    title = ""

print("\nCalculating your BMI and Ideal Weight Range...")
print("-------------------------------")

print(f"{title} {name}, aged {age}, your BMI is: {bmi:.2f}")
print(f"You are in the '{bmi_category}' category.")
print(f"The ideal weight range for your height is between {ideal_weight_range[0]:.2f} kg and {ideal_weight_range[1]:.2f} kg.")
print(f"{weight_goal}")
print(f"{caloric_intake_suggestion}")

print("Thank you for using the Enhanced BMI Calculator. Stay healthy!")
