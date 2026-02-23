# Inventory Management System

def remove_zero_stock(stocks):
    """Remove items with 0 stock"""
    available = []

    for s in stocks:
        if s > 0:
            available.append(s)

    return available


def restock_items(stocks):
    """Add 50 units to items below 10"""
    updated = []

    for s in stocks:
        if s < 10:
            updated.append(s + 50)
        else:
            updated.append(s)

    return updated


def total_inventory(stocks):
    """Calculate total inventory"""
    return sum(stocks)


# ---------------- MAIN PROGRAM ----------------

# Input
n = int(input("Enter number of products: "))

stocks = []

for i in range(n):
    s = int(input(f"Enter stock of product {i+1}: "))
    stocks.append(s)

print("\nOriginal Stock:", stocks)

# Remove zero stock
available_stock = remove_zero_stock(stocks)
print("After Removing Zero Stock:", available_stock)

# Restock low items
restocked_stock = restock_items(available_stock)
print("After Restocking (<10 +50):", restocked_stock)

# Total inventory
total = total_inventory(restocked_stock)

print("\n--- Inventory Summary ---")
print("Total Inventory Count:", total)