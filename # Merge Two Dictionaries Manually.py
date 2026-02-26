# Merge Two Dictionaries Manually

n1 = int(input("Enter number of elements in first dictionary: "))
dict1 = {}

for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

n2 = int(input("Enter number of elements in second dictionary: "))
dict2 = {}

for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

merged = {}

for k in dict1:
    merged[k] = dict1[k]

for k in dict2:
    merged[k] = dict2[k]   # Overwrites if key already exists

print("Merged Dictionary =", merged)