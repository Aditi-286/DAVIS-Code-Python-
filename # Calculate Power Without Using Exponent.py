# Calculate Power Without Using Exponent Operator

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1

for i in range(exp):
    result *= base

print("Result =", result)