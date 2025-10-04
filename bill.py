# Program to calculate electricity bill

# Input: number of units consumed
units = float(input("Enter the number of units consumed: "))

# Rate per unit
rate = 5  # ₹5 per unit

# Calculate total bill
bill = units * rate

# Display result
print(f"Electricity Bill = ₹{bill:.2f}")
