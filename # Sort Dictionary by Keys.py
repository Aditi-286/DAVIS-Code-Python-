# Sort Dictionary by Keys

n = int(input("Enter number of elements: "))

data = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

sorted_dict = {}

for key in sorted(data):
    sorted_dict[key] = data[key]

print("Sorted by Keys =", sorted_dict)