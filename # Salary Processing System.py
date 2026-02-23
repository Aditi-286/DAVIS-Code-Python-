# Salary Processing System

def remove_below_min_wage(salaries, min_wage):
    """Remove salaries below minimum wage"""
    valid_salaries = []

    for s in salaries:
        if s >= min_wage:
            valid_salaries.append(s)

    return valid_salaries


def add_bonus(salaries):
    """Add 5% bonus to salaries above 50,000"""
    updated = []

    for s in salaries:
        if s > 50000:
            bonus_salary = s * 1.05   # 5% bonus
            updated.append(bonus_salary)
        else:
            updated.append(s)

    return updated


def get_top_3(salaries):
    """Get top 3 highest salaries"""
    salaries.sort(reverse=True)
    return salaries[:3]


# ---------------- MAIN PROGRAM ----------------

# Input
n = int(input("Enter number of employees: "))
min_wage = float(input("Enter minimum wage: "))

salaries = []

for i in range(n):
    s = float(input(f"Enter salary of employee {i+1}: ₹"))
    salaries.append(s)

print("\nOriginal Salaries:", salaries)

# Remove below minimum wage
valid_salaries = remove_below_min_wage(salaries, min_wage)
print("After Removing Below Minimum Wage:", valid_salaries)

# Add bonus
bonus_salaries = add_bonus(valid_salaries)
print("After Adding Bonus:", bonus_salaries)

# Sort descending
bonus_salaries.sort(reverse=True)
print("Sorted Salaries (Descending):", bonus_salaries)

# Top 3 salaries
top_3 = get_top_3(bonus_salaries)

print("\n--- Final Result ---")
print("Top 3 Highest Salaries:", top_3)