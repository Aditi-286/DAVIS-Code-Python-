# Read character
ch = input().lower()

# Check vowel or consonant
if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Invalid Input")