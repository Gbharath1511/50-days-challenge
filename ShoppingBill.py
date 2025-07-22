# Total Cost Calculator with Tax

# Get prices of three items
item1 = float(input("Enter price of item 1: ₹"))
item2 = float(input("Enter price of item 2: ₹"))
item3 = float(input("Enter price of item 3: ₹"))

# Get tax percentage
tax_percent = float(input("Enter tax percentage (e.g., 18 for 18%): "))

# Calculate subtotal
subtotal = item1 + item2 + item3

# Calculate tax
tax_amount = subtotal * (tax_percent / 100)

# Calculate total cost
total_cost = subtotal + tax_amount

# Display the result
print(f"\nSubtotal: ₹{subtotal:.2f}")
print(f"Tax (@{tax_percent}%): ₹{tax_amount:.2f}")
print(f"Total cost including tax: ₹{total_cost:.2f}")
