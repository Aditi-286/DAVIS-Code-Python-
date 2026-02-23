# Temperature Monitoring System

def find_hottest_coldest(temps):
    """Find hottest and coldest temperature"""
    hottest = max(temps)
    coldest = min(temps)
    return hottest, coldest


def mark_heat_alert(temps):
    """Replace temperatures above 45°C with 'Heat Alert'"""
    updated = []

    for t in temps:
        if t > 45:
            updated.append("Heat Alert")
        else:
            updated.append(t)

    return updated


def count_extreme_days(temps):
    """Count days above 40°C"""
    count = 0

    for t in temps:
        if isinstance(t, (int, float)) and t > 40:
            count += 1

    return count


# ---------------- MAIN PROGRAM ----------------

# Input
days = int(input("Enter number of days in month: "))

temperatures = []

for i in range(days):
    t = float(input(f"Enter temperature of Day {i+1} (°C): "))
    temperatures.append(t)

print("\nOriginal Temperatures:", temperatures)

# Find hottest & coldest
hottest, coldest = find_hottest_coldest(temperatures)

# Mark heat alerts
alert_temps = mark_heat_alert(temperatures)

# Count extreme days
extreme_count = count_extreme_days(temperatures)

# Display results
print("\n--- Temperature Report ---")
print("Hottest Temperature:", hottest, "°C")
print("Coldest Temperature:", coldest, "°C")

print("After Heat Alert Marking:", alert_temps)

print("Extreme Days (>40°C):", extreme_count)
