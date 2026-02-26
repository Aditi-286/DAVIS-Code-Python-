# Separate Even and Odd Numbers from List

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

even = []
odd = []

for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers =", even)
print("Odd numbers =", odd)