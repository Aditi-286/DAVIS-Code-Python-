# Perform Union of Two Sets

n1 = int(input("Enter number of elements in first set: "))
set1 = set()

for i in range(n1):
    set1.add(input("Enter element: "))

n2 = int(input("Enter number of elements in second set: "))
set2 = set()

for i in range(n2):
    set2.add(input("Enter element: "))

union_set = set1 | set2

print("Set 1 =", set1)
print("Set 2 =", set2)
print("Union =", union_set)