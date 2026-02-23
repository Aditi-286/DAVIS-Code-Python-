# Bank Transaction Analyzer

def calculate_balance(transactions):
    """Calculate total balance"""
    return sum(transactions)


def largest_withdrawal(transactions):
    """Find largest withdrawal (most negative value)"""
    withdrawals = []

    for t in transactions:
        if t < 0:
            withdrawals.append(t)

    if len(withdrawals) == 0:
        return 0

    return min(withdrawals)   # Most negative = largest withdrawal


def count_large_deposits(transactions, limit=10000):
    """Count deposits greater than 10,000"""
    count = 0

    for t in transactions:
        if t > limit:
            count += 1

    return count


# ---------------- MAIN PROGRAM ----------------

# Input
n = int(input("Enter number of transactions: "))

transactions = []

for i in range(n):
    t = float(input(f"Enter transaction {i+1} (use - for withdrawal): ₹"))
    transactions.append(t)

print("\nTransactions:", transactions)

# Calculate balance
balance = calculate_balance(transactions)

# Find largest withdrawal
largest_wd = largest_withdrawal(transactions)

# Count big deposits
big_deposits = count_large_deposits(transactions)

# Display result
print("\n--- Bank Summary ---")
print("Total Balance: ₹", balance)

if largest_wd != 0:
    print("Largest Withdrawal: ₹", largest_wd)
else:
    print("No withdrawals found.")

print("Deposits > ₹10,000:", big_deposits)