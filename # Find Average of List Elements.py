# Find Average of List Elements

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

total = 0

for num in lst:
    total += num

average = total / n

print("Average =", average)