# Online Exam Result Processor

def remove_lowest_two(scores):
    """Remove lowest 2 scores"""
    scores.sort()
    return scores[2:]   # Remove first two lowest


def add_grace_marks(scores):
    """Add 5 grace marks to students scoring between 30 and 35"""
    updated = []

    for s in scores:
        if 30 <= s <= 35:
            updated.append(s + 5)
        else:
            updated.append(s)

    return updated


def count_passed(scores, pass_mark=40):
    """Count students who passed"""
    count = 0

    for s in scores:
        if s >= pass_mark:
            count += 1

    return count


# ---------------- MAIN PROGRAM ----------------

# Input
n = int(input("Enter number of students: "))

scores = []

for i in range(n):
    s = int(input(f"Enter score of student {i+1}: "))
    scores.append(s)

print("\nOriginal Scores:", scores)

# Remove lowest 2 scores
if len(scores) < 3:
    print("Not enough students to process.")
else:
    scores_after_removal = remove_lowest_two(scores)
    print("After Removing Lowest 2 Scores:", scores_after_removal)

    # Add grace marks
    scores_after_grace = add_grace_marks(scores_after_removal)
    print("After Adding Grace Marks:", scores_after_grace)

    # Count passed students
    passed = count_passed(scores_after_grace)

    print("\n--- Final Result ---")
    print("Number of Students Passed (>=40):", passed)