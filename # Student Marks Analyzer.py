# Student Marks Analyzer

def remove_invalid_marks(marks):
    """Remove marks less than 0 or greater than 100"""
    valid_marks = []
    for m in marks:
        if 0 <= m <= 100:
            valid_marks.append(m)
    return valid_marks


def calculate_average(marks):
    """Calculate average of marks"""
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)


def find_toppers(marks):
    """Find highest score(s)"""
    highest = max(marks)
    toppers = []

    for m in marks:
        if m == highest:
            toppers.append(m)

    return highest, toppers


def get_grade(average):
    """Return grade based on average"""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# ---------------- MAIN PROGRAM ----------------

# Input marks from user
n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = float(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

print("\nOriginal Marks:", marks)

# Remove invalid marks
valid_marks = remove_invalid_marks(marks)

print("Valid Marks:", valid_marks)

# Check if valid marks exist
if len(valid_marks) == 0:
    print("No valid marks available.")
else:
    # Calculate average
    avg = calculate_average(valid_marks)

    # Find toppers
    highest, toppers = find_toppers(valid_marks)

    # Get grade
    grade = get_grade(avg)

    # Display results
    print("\n--- Result ---")
    print("Average Marks:", round(avg, 2))
    print("Highest Marks:", highest)
    print("Topper(s):", toppers)
    print("Grade:", grade)