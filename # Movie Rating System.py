# Movie Rating System

def remove_invalid_ratings(ratings):
    """Remove ratings less than 1 or greater than 5"""
    valid = []

    for r in ratings:
        if 1 <= r <= 5:
            valid.append(r)

    return valid


def calculate_average(ratings):
    """Calculate average rating"""
    if len(ratings) == 0:
        return 0
    return sum(ratings) / len(ratings)


def count_five_star(ratings):
    """Count number of 5-star ratings"""
    count = 0

    for r in ratings:
        if r == 5:
            count += 1

    return count


def sort_ratings(ratings):
    """Sort ratings in ascending order"""
    return sorted(ratings)


# ---------------- MAIN PROGRAM ----------------

# Input
n = int(input("Enter number of ratings: "))

ratings = []

for i in range(n):
    r = int(input(f"Enter rating {i+1} (1 to 5): "))
    ratings.append(r)

print("\nOriginal Ratings:", ratings)

# Remove invalid ratings
valid_ratings = remove_invalid_ratings(ratings)
print("Valid Ratings:", valid_ratings)

# Check if valid ratings exist
if len(valid_ratings) == 0:
    print("No valid ratings available.")
else:
    # Average rating
    avg = calculate_average(valid_ratings)

    # Count 5-star ratings
    five_star = count_five_star(valid_ratings)

    # Sort ratings
    sorted_ratings = sort_ratings(valid_ratings)

    # Display result
    print("\n--- Movie Rating Report ---")
    print("Average Rating:", round(avg, 2))
    print("5-Star Ratings Count:", five_star)
    print("Sorted Ratings:", sorted_ratings)