# Create Student Marks Dictionary and Find Topper

n = int(input("Enter number of students: "))

marks = {}

for i in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter marks: "))
    marks[name] = score

topper = max(marks, key=marks.get)

print("Marks Dictionary =", marks)
print("Topper =", topper)
print("Highest Marks =", marks[topper])