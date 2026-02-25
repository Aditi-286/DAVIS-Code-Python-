# Read character
ch = input()

# Check digit or alphabet
if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Special Character")