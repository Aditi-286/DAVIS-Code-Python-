# Find First Non-Repeating Character in String

text = input("Enter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

found = False

for ch in text:
    if freq[ch] == 1:
        print("First non-repeating character =", ch)
        found = True
        break

if not found:
    print("No non-repeating character found")