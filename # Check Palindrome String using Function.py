# Check Palindrome String using Function

def is_palindrome(text):
    return text == text[::-1]


s = input("Enter a string: ")

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")