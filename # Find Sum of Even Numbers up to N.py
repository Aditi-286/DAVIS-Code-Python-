# Find Sum of Even Numbers up to N

n = int(input("Enter N: "))

sum_even = 0
i = 2

while i <= n:
    sum_even += i
    i += 2

print("Sum of even numbers =", sum_even)