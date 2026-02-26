# Count Number of Words in a Sentence

text = input("Enter a sentence: ")

words = text.split()
count = 0

for w in words:
    count += 1

print("Number of words =", count)