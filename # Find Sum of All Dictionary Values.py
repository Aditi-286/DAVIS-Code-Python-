# Find Sum of All Dictionary Values

n = int(input("Enter number of elements: "))

data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

total = 0

for v in data.values():
    total += v

print("Sum of values =", total)