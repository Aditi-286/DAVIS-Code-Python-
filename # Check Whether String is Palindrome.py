# Check Whether String is Palindrome

text = input("Enter a string: ")

rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome String")
else:
    print("Not a Palindrome String")