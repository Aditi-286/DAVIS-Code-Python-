# Reverse a String using For Loop

text = input("Enter a string: ")

rev = ""

for ch in text:
    rev = ch + rev

print("Reversed string =", rev)