'''
Exercise 4: Sales List Analysis
Student: Agrim Shiwakoti
Day: 2
'''

#input values
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

#comprehensions and conversions
sorted_sales = sorted(monthly_sales)

greater_than_100k = [sale for sale in monthly_sales if sale > 100000]

sales_with_tax = [float(f"{sale * 1.13:.2f}") for sale in monthly_sales] #converting to float and rounding to 2 dp

total_sales = sum(monthly_sales)

average_sales = total_sales / len(monthly_sales)

# Output
print(f"Sorted Sales: {sorted_sales}")
print(f"Sales Greater Than Rs. 1,00,000: {greater_than_100k}")
print(f"Sales With Tax: {sales_with_tax}")
print(f"Total Sales: Rs. {total_sales}")
print(f"Average Sales: Rs. {average_sales}")