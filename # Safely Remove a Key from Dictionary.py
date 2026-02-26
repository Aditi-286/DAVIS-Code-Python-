# Safely Remove a Key from Dictionary

n = int(input("Enter number of elements: "))

data = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

remove_key = input("Enter key to remove: ")

if remove_key in data:
    del data[remove_key]
    print("Key removed successfully")
else:
    print("Key not found")

print("Updated Dictionary =", data)
