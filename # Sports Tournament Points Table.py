# Sports Tournament Points Table

def replace_negative(points):
    """Replace negative points with 0"""
    updated = []

    for p in points:
        if p < 0:
            updated.append(0)
        else:
            updated.append(p)

    return updated


def find_winner_runnerup(points):
    """Find winner and runner-up"""
    sorted_points = sorted(points, reverse=True)

    winner = sorted_points[0]
    runner_up = sorted_points[1] if len(sorted_points) > 1 else None

    return winner, runner_up


def sort_leaderboard(points):
    """Sort leaderboard in descending order"""
    return sorted(points, reverse=True)


# ---------------- MAIN PROGRAM ----------------

# Input
n = int(input("Enter number of teams: "))

points = []

for i in range(n):
    p = int(input(f"Enter points for Team {i+1}: "))
    points.append(p)

print("\nOriginal Points:", points)

# Replace negative points
valid_points = replace_negative(points)
print("After Replacing Negative Points:", valid_points)

# Find winner and runner-up
if len(valid_points) < 2:
    print("Not enough teams to find winner and runner-up.")
else:
    winner, runner_up = find_winner_runnerup(valid_points)

    # Sort leaderboard
    leaderboard = sort_leaderboard(valid_points)

    # Display result
    print("\n--- Tournament Leaderboard ---")
    print("Sorted Leaderboard:", leaderboard)
    print("Winner Points:", winner)
    print("Runner-Up Points:", runner_up)