# Reverse a List Without reverse() Method

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(input("Enter element: "))

rev = []

for i in range(n - 1, -1, -1):
    rev.append(lst[i])

print("Reversed list =", rev)