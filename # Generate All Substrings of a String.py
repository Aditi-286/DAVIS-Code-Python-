# Generate All Substrings of a String

text = input("Enter a string: ")

n = len(text)

print("Substrings:")

for i in range(n):
    for j in range(i + 1, n + 1):
        print(text[i:j])