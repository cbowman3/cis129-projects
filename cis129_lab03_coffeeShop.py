# Input for amount of coffee and muffins
Coffee_count = int(input("Number of coffees bought? "))
Tea_count = int(input("Number of teas bought? "))
Muffin_count = int(input("Number of muffins bought? "))
Donut_count = int(input("Number of donuts bought? "))

# Set default values for testing
# Coffee_count = 4
# Muffin_count = 5
# Tea_count = 2
# Donut_count = 2

# Calculation of total cost of muffins, coffee with sales tax
Coffee_price = 4
Tea_price = 3
Muffin_price = 3
Donut_price = 2
Tax_rate = 0.06

Coffee_cost = Coffee_count * Coffee_price
Tea_cost = Tea_count * Tea_price
Muffin_cost = Muffin_count * Muffin_price
Donut_cost = Donut_count * Donut_price
Subtotal = Coffee_cost + Tea_cost + Muffin_cost + Donut_cost
Tax = Subtotal * Tax_rate
Total_cost = Subtotal + Tax

# Display receipt
print('My Coffee Shop Receipt')

# Display individual items and costs
print('Coffee quantity:', Coffee_count)
print('Coffee cost: $', Coffee_cost)

print('Tea:', Tea_count)
print('Tea cost: $', Tea_cost)

print('Muffin quantity:', Muffin_count)
print('Muffin cost: $', Muffin_cost)

print('Donut quantity:', Coffee_count)
print('Donut cost: $', Donut_cost)

# Display tax and total
print('Tax: $', Tax)
print('Total Cost: $', Total_cost)

# Display thank you message 
print('Thank you, come again!')

