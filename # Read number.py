# Read number
num = int(input())

# Check using bitwise operator
if num & 1 == 0:
    print("Even")
else:
    print("Odd")