# Check Whether One Set is Subset of Another

n1 = int(input("Enter number of elements in first set: "))
set1 = set()

for i in range(n1):
    set1.add(input("Enter element: "))

n2 = int(input("Enter number of elements in second set: "))
set2 = set()

for i in range(n2):
    set2.add(input("Enter element: "))

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")