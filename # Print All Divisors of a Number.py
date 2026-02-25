# Print All Divisors of a Number

n = int(input("Enter a number: "))

print("Divisors are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")