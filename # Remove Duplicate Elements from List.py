# Remove Duplicate Elements from List

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

print("List without duplicates =", unique)