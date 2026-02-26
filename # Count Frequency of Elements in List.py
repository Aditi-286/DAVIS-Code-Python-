# Count Frequency of Elements in List

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(input("Enter element: "))

freq = {}

for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Frequencies:")

for key, value in freq.items():
    print(key, ":", value)