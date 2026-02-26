# Sort a List Without Using sort() Method

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

for i in range(n):
    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted list =", lst)