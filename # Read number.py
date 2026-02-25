# Read number
num = int(input())

sum_digits = 0
n = abs(num)  # Handle negative numbers

while n > 0:
    sum_digits += n % 10
    n //= 10

print(sum_digits)