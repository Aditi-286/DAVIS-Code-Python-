# Create Dictionary from Two Lists

n = int(input("Enter number of elements: "))

keys = []
values = []

print("Enter keys:")
for i in range(n):
    keys.append(input())

print("Enter values:")
for i in range(n):
    values.append(input())

data = {}

for i in range(n):
    data[keys[i]] = values[i]

print("Dictionary =", data)