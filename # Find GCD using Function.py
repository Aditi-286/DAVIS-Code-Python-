# Find GCD using Function

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD =", gcd(x, y))