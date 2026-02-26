# Find Frequency of Each Character in String

text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequencies:")

for k, v in freq.items():
    print(k, ":", v)