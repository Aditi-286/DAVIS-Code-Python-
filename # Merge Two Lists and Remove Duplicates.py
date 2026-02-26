# Merge Two Lists and Remove Duplicates

n1 = int(input("Enter number of elements in first list: "))

list1 = []

for i in range(n1):
    list1.append(int(input("Enter element: ")))

n2 = int(input("Enter number of elements in second list: "))

list2 = []

for i in range(n2):
    list2.append(int(input("Enter element: ")))

merged = list1 + list2
unique = []

for item in merged:
    if item not in unique:
        unique.append(item)

print("Merged list without duplicates =", unique)