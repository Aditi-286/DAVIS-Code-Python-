# Find Symmetric Difference of Two Sets

n1 = int(input("Enter number of elements in first set: "))
set1 = set()

for i in range(n1):
    set1.add(input("Enter element: "))

n2 = int(input("Enter number of elements in second set: "))
set2 = set()

for i in range(n2):
    set2.add(input("Enter element: "))

sym_diff = set1 ^ set2

print("Symmetric Difference =", sym_diff)