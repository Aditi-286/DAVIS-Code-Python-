# Find Common Elements Between Two Lists

n1 = int(input("Enter number of elements in first list: "))
list1 = []

for i in range(n1):
    list1.append(int(input("Enter element: ")))

n2 = int(input("Enter number of elements in second list: "))
list2 = []

for i in range(n2):
    list2.append(int(input("Enter element: ")))

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements =", common)