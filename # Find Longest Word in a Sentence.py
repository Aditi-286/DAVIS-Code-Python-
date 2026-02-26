# Find Longest Word in a Sentence

text = input("Enter a sentence: ")

words = text.split()

longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print("Longest word =", longest)