# Find Maximum Value in a Tuple

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

tup = tuple(lst)

maximum = tup[0]

for num in tup:
    if num > maximum:
        maximum = num

print("Tuple =", tup)
print("Maximum =", maximum)