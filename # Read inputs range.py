# Read inputs
num = int(input())
low = int(input())
high = int(input())

# Check range
if low <= num <= high:
    print("Within Range")
else:
    print("Out of Range")