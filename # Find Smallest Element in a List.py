# Find Smallest Element in a List

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

smallest = lst[0]

for num in lst:
    if num < smallest:
        smallest = num

print("Smallest element =", smallest)