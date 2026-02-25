# Read input
weight = float(input())   # in kg
height = float(input())   # in meters

# Calculate BMI
bmi = weight / (height ** 2)

# Check category
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")