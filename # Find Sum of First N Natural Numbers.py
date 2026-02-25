# Find Sum of First N Natural Numbers

n = int(input("Enter N: "))

sum_n = 0

for i in range(1, n + 1):
    sum_n += i

print("Sum =", sum_n)