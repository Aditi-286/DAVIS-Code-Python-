# Check Whether Tuple Elements Are Unique

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(input("Enter element: "))

tup = tuple(lst)

unique = True

for i in range(len(tup)):
    for j in range(i + 1, len(tup)):
        if tup[i] == tup[j]:
            unique = False
            break

if unique:
    print("All elements are unique")
else:
    print("Elements are not unique")