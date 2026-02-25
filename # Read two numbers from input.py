# Read two numbers from input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap without using third variable
a = a + b
b = a - b
a = a - b

# Print result
print("After swapping:")
print("a =", a)
print("b =", b)