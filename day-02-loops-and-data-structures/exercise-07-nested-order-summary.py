'''
Exercise 7: Nested Order Summary
Student: Agrim Shiwakoti
Day: 2
'''

#input values
orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# order id and customer
print("Order Summary:")
for order_id, order_details in orders.items():
    print(f"Order ID: {order_id}, Customer: {order_details['customer']}")

completed_amount = 0 #global variable
pending_count = 0 #global variable
print(f"\nOrders with status 'Completed':")
for order_id, order_details in orders.items():
    if order_details['status'] == "Completed":
        print(order_id, order_details)
        completed_amount += order_details['amount']
    else:
        pending_count += 1

print(f"\nTotal Amount from Completed Orders: Rs. {completed_amount}")
print(f"Total Number of Pending Orders: {pending_count}")

#adding new order
new_order_id = "ORD-004"
new_order_details = {
    "customer": "Mahesh",
    "amount": 4800,
    "status": "Pending"
}
orders[new_order_id] = new_order_details
print("\nNew Order List")
for order_id, order_details in orders.items():
    print(f"Order ID: {order_id}, Customer: {order_details['customer']}")