#!/usr/bin/env python3

# Display a welcome message
print("The invoice program")
print()

# Get user entries
customer_type = input("Enter customer type (r/w):\t")
invoice_total = float(input("Enter invoice total:\t\t"))
print()

# Determine discounts for Retail customers
if customer_type.lower() == "r":
    if invoice_total > 0 and invoice_total < 100:
        discount_percent = 0
    elif invoice_total >= 100 and invoice_total < 250:
        discount_percent = .1
    elif invoice_total >= 250 and invoice_total < 500:
        discount_percent = .2
    elif invoice_total >= 500:
        discount_percent = .25

# Determine discounts for Wholesale customers
elif customer_type.lower() == "w":
    if invoice_total > 0 and invoice_total < 500:
        discount_percent = .4
    elif invoice_total >= 500:
        discount_percent = .5

# Set discount to zero if neither Retail or Wholesale
else:
    discount_percent = 0

# Calculate discount amount and new invoice total
discount_amount = round(invoice_total * discount_percent, 2)
new_invoice_total = invoice_total - discount_amount

# Display the results
print(f"Invoice total:\t\t{invoice_total}")
print(f"Discount percent:\t{discount_percent}")
print(f"Discount amount:\t{discount_amount}")
print(f"New invoice total:\t{new_invoice_total}")
print()
print("Bye!")