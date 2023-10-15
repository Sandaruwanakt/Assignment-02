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

def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    elif gender == "Female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
    return bmr

def calculate_tdee(bmr, activity_level):
    activity_factors = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Super Active": 1.9
    }
    return bmr * activity_factors.get(activity_level, 1.2)

def suggest_daily_caloric_intake(tdee, weight_goal):
    if weight_goal.startswith("You are under"):
        return f"To {weight_goal.lower()} and achieve your ideal weight, consume {tdee + 500:.0f} calories per day."
    elif weight_goal.startswith("You are above"):
        return f"To {weight_goal.lower()} and achieve your ideal weight, consume {tdee - 500:.0f} calories per day."
    else:
        return f"To {weight_goal.lower()} and maintain your ideal weight, consume {tdee:.0f} calories per day."

def get_name():
    name = input("Enter your name: ")
    while not name.isalpha():
        print("Invalid input. Please enter a valid name with alphabetic characters only.")
        name = input("Enter your name: ")
    return name

def get_gender():
    gender = input("Enter your gender (Male/Female): ").strip().title()
    while gender not in ["Male", "Female"]:
        print("Invalid input. Please enter 'Male' or 'Female' for gender.")
        gender = input("Enter your gender (Male/Female): ").strip().title()
    return gender

def get_age():
    age = input("Enter your age: ")
    while not age.isdigit():
        print("Invalid input. Please enter a valid age (numeric value).")
        age = input("Enter your age: ")
    return int(age)

def get_weight():
    weight = input("Enter your weight in kilograms: ")
    while not weight.replace(".", "", 1).isdigit():  # Allowing decimal point for weight
        print("Invalid input. Please enter a valid weight (numeric value).")
        weight = input("Enter your weight in kilograms: ")
    return float(weight)

def get_height():
    height = input("Enter your height in meters: ")
    while not height.replace(".", "", 1).isdigit():  # Allowing decimal point for height
        print("Invalid input. Please enter a valid height (numeric value).")
        height = input("Enter your height in meters: ")
    return float(height)

def get_activity_level():
    activity_levels = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Super Active"]
    activity_level = input("Enter your activity level (Sedentary/Lightly Active/Moderately Active/Very Active/Super Active): ").strip().title()
    while activity_level not in activity_levels:
        print("Invalid input. Please select from the provided activity levels.")
        activity_level = input("Enter your activity level: ").strip().title()
    return activity_level

print("Welcome to the Enhanced BMI Calculator!")
print("-------------------------------")

name = get_name()
gender = get_gender()
age = get_age()
weight = get_weight()
height = get_height()

bmi = calculate_bmi(weight, height)
bmi_category = interpret_bmi(bmi)
ideal_weight_range = calculate_ideal_weight_range(height)
weight_goal = suggest_weight_goal(weight, ideal_weight_range)
caloric_intake_suggestion = suggest_caloric_intake(bmi_category)

bmr = calculate_bmr(weight, height, age, gender)
activity_level = get_activity_level()
tdee = calculate_tdee(bmr, activity_level)
daily_caloric_intake_suggestion = suggest_daily_caloric_intake(tdee, weight_goal)

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

print("\nCalculating your Daily Caloric Intake...")
print("-------------------------------")

print(f"Your Basal Metabolic Rate (BMR) is: {bmr:.2f} calories/day.")
print(f"Your Total Daily Energy Expenditure (TDEE) is: {tdee:.2f} calories/day.")
print(f"{daily_caloric_intake_suggestion}")

print("Thank you for using the Enhanced BMI Calculator. Stay healthy!")
