# E-Commerce Cart System

def remove_duplicates(prices):
    """Remove duplicate prices"""
    return list(set(prices))


def apply_discount(total):
    """Apply 10% discount if total > 5000"""
    if total > 5000:
        return total * 0.90   # 10% discount
    return total


def add_gst(amount):
    """Add 18% GST"""
    return amount * 1.18


# ---------------- MAIN PROGRAM ----------------

# Input number of products
n = int(input("Enter number of products: "))

prices = []

# Input prices
for i in range(n):
    p = float(input(f"Enter price of product {i+1}: ₹"))
    prices.append(p)

print("\nOriginal Cart:", prices)

# Remove duplicates
unique_prices = remove_duplicates(prices)
print("After Removing Duplicates:", unique_prices)

# Calculate total
total = sum(unique_prices)
print("Total Amount: ₹", total)

# Apply discount
discounted_total = apply_discount(total)

if discounted_total != total:
    print("10% Discount Applied")

print("After Discount: ₹", discounted_total)

# Add GST
final_amount = add_gst(discounted_total)

# Display final amount
print("\n--- Final Bill ---")
print("Final Payable Amount (Including 18% GST): ₹", round(final_amount, 2))