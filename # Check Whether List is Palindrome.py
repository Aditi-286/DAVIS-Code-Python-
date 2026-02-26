# Check Whether List is Palindrome

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(input("Enter element: ")))

if lst == lst[::-1]:
    print("Palindrome List")
else:
    print("Not a Palindrome List")