# Program to calculate electricity bill

# Input: number of units consumed
units = float(input("Enter the number of units consumed: "))

# Rate per unit
rate = 5  # ₹5 per unit

# Calculate total bill
bill = units * rate

# Display result
print(f"Electricity Bill = ₹{bill:.2f}")

# Program to calculate final amount after discount

# Take input from user
amount = float(input("Enter the total purchase amount: "))

# Check if discount is applicable
if amount > 1000:
    discount = amount * 0.10   # 10% discount
    final_amount = amount - discount
    print(f"Discount of ₹{discount:.2f} applied!")
else:
    discount = 0
    final_amount = amount
    print("No discount applied.")

# Display final bill
print(f"Final Amount to Pay: ₹{final_amount:.2f}")
