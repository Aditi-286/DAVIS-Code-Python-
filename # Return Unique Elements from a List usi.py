# Return Unique Elements from a List using Function

def unique_elements(lst):
    unique = []

    for item in lst:
        if item not in unique:
            unique.append(item)

    return unique


n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

print("Unique elements =", unique_elements(lst))