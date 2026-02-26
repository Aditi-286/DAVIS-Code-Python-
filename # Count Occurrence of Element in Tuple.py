# Count Occurrence of Element in Tuple

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(input("Enter element: "))

tup = tuple(lst)

key = input("Enter element to count: ")

count = 0

for item in tup:
    if item == key:
        count += 1

print("Tuple =", tup)
print("Occurrence of", key, "=", count)