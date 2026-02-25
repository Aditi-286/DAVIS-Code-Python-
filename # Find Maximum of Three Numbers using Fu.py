# Find Maximum of Three Numbers using Function

def maximum(a, b, c):
    return max(a, b, c)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Maximum =", maximum(x, y, z))