# Check Whether Key Exists in Dictionary

n = int(input("Enter number of elements: "))

data = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

search_key = input("Enter key to search: ")

if search_key in data:
    print("Key exists in dictionary")
else:
    print("Key does not exist")