# Attendance Tracker

def calculate_percentage(attendance):
    """Calculate attendance percentage"""
    total_days = len(attendance)
    present_days = sum(attendance)

    if total_days == 0:
        return 0

    return (present_days / total_days) * 100


def find_low_attendance_students(percentages, threshold=75):
    """Find students below given percentage"""
    low_attendance = []

    for i in range(len(percentages)):
        if percentages[i] < threshold:
            low_attendance.append(i + 1)  # Student number

    return low_attendance


def mark_consecutive_absences(attendance):
    """Replace 2 or more consecutive absences with WARNING"""
    flagged = attendance.copy()

    count = 0

    for i in range(len(attendance)):
        if attendance[i] == 0:
            count += 1
            if count >= 2:
                flagged[i] = "WARNING"
        else:
            count = 0

    return flagged


# ---------------- MAIN PROGRAM ----------------

students = int(input("Enter number of students: "))
days = int(input("Enter number of days: "))

attendance_data = []
percentages = []

# Input attendance for each student
for i in range(students):
    print(f"\nEnter attendance for Student {i+1} (1 = Present, 0 = Absent)")

    record = []
    for j in range(days):
        val = int(input(f"Day {j+1}: "))
        record.append(val)

    attendance_data.append(record)

# Process each student
for i in range(students):
    percent = calculate_percentage(attendance_data[i])
    percentages.append(percent)

# Display results
print("\n--- Attendance Report ---")

for i in range(students):
    print(f"\nStudent {i+1}")
    print("Attendance:", attendance_data[i])
    print("Percentage:", round(percentages[i], 2), "%")

    if percentages[i] < 75:
        print("Status: Below 75% ⚠️")
    else:
        print("Status: Eligible ✅")

    flagged = mark_consecutive_absences(attendance_data[i])
    print("After Warning Flag:", flagged)

# Show list of low attendance students
low_students = find_low_attendance_students(percentages)

print("\nStudents Below 75% Attendance:", low_students)