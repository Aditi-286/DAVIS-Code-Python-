# Remove Duplicate Characters from String

text = input("Enter a string: ")

result = ""
seen = ""

for ch in text:
    if ch not in seen:
        seen += ch
        result += ch

print("String without duplicates =", result)