# Find Minimum Value in a Tuple

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

tup = tuple(lst)

minimum = tup[0]

for num in tup:
    if num < minimum:
        minimum = num

print("Tuple =", tup)
print("Minimum =", minimum)