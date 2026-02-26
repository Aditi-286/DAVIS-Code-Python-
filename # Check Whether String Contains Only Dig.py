# Check Whether String Contains Only Digits

text = input("Enter a string: ")

is_digit = True

for ch in text:
    if ch < '0' or ch > '9':
        is_digit = False
        break

if is_digit:
    print("String contains only digits")
else:
    print("String does not contain only digits")