# Replace All Vowels with *

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
result = ""

for ch in text:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print("Updated string =", result)