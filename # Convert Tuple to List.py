# Convert Tuple to List

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(input("Enter element: ")))

tup = tuple(lst)

new_list = list(tup)

print("Tuple =", tup)
print("List =", new_list)