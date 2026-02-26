# Find Key with Maximum Value in Dictionary

n = int(input("Enter number of elements: "))

data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

max_key = None
max_value = float('-inf')

for k, v in data.items():
    if v > max_value:
        max_value = v
        max_key = k

print("Dictionary =", data)
print("Key with maximum value =", max_key)
print("Maximum value =", max_value)