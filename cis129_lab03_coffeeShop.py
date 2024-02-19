# Input for amount of coffee and muffins
Coffee_count = int(input("Number of coffees bought? "))
Muffin_count = int(input("Number of muffins bought? "))

# Set default values for testing
# Coffee_count = 4
# Muffin_count = 5

# Calculation of total cost of muffins, coffee with sales tax
Coffee_price = 4
Muffin_price = 3
Tax_rate = 0.06

Coffee_cost = Coffee_count * Coffee_price
Muffin_cost = Muffin_count * Muffin_price
Subtotal = Coffee_cost + Muffin_cost
Tax = Subtotal * Tax_rate
Total_cost = Subtotal + Tax

# Display receipt
print('My Coffee and Muffin Shop Receipt')

# Display individual items and costs
print('Coffee quantity:', Coffee_count)
print('Coffee cost: $', Coffee_cost)

print('Muffin quantity:', Muffin_count)
print('Muffin cost: $', Muffin_cost)

# Display tax and total
print('Tax: $', Tax)
print('Total Cost: $', Total_cost)
