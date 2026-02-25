# Read number
num = int(input())

rev = 0
n = abs(num)

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

# Handle negative number
if num < 0:
    rev = -rev

print(rev)