# Convert String to Title Case Manually

text = input("Enter a string: ")

result = ""
new_word = True

for ch in text:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            result += ch.upper()
            new_word = False
        else:
            result += ch.lower()

print("Title Case =", result)