# Sort Dictionary by Values

n = int(input("Enter number of elements: "))

data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

sorted_items = sorted(data.items(), key=lambda x: x[1])

sorted_dict = {}

for key, value in sorted_items:
    sorted_dict[key] = value

print("Sorted by Values =", sorted_dict)