# Read number
num = int(input())

# Check divisibility
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not Divisible by both 3 and 5")