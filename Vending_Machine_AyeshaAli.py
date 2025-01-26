# Vending Machince Program

# Define a list of available items with their prices
items =[{"name": "Candy", "price": 0.50},
    {"name": "Water", "price": 1.00},
    {"name": "Lays Chips", "price": 0.75},
    {"name": "Coke", "price": 3.00},
    {"name": "Galaxy Chocolate", "price": 2.00},
    {"name": "Apple", "price": 1.00},
    {"name": "Banana", "price": 1.00},
    {"name": "Sandwich", "price": 2.00},
    {"name": "Mango Juice", "price": 1.50},
    {"name": "Cookies", "price": 3.00}]

# Print the list of available items
def display_items():
    print("Welcome to the Vending Machine!\n")
    print("Here is a list of available items:")
    for i, item in enumerate(items):
        print(f"{i+1}. {item['name']} - ${item['price']:.2f}")

# Allow the user to select and add items to their purchase
def select_items():
    selected_items = []
    total_price = 0.0
    while True:
        display_items()
        print("\nEnter your choice (1-10), or '0' to exit:")
        choice = input()
        if choice == "0":
            break
        else:
            try:
                choice = int(choice)
                if choice > 0 and choice <= len(items):
                    selected_items.append(items[choice - 1])
                    total_price += items[choice - 1]['price']
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return selected_items, total_price

# Accept payment and give change
def make_payment(total_price):
    payment = 0.0
    while payment < total_price:
        print(f"\nYour total is ${total_price:.2f}. Please insert payment:")
        try:
            payment += float(input())
            if payment < total_price:
                print("Insufficient payment. Please insert more money.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
        return payment - total_price

# Print a recipient for the purchase
def print_receipt(selected_items, total_price, payment, change):
    print("\nThank you for your purchase! Here is your receipt:")
    for item in selected_items:
        print(f"{item['name']}: ${item['price']:.2f}")
    print(f"\nTotal: ${total_price:.2f}")
    print(f"Payment: ${payment:.2f}")
    print(f"Change: ${change:.2f}")

# Run the vending machine program
selected_items, total_price = select_items()
payment = make_payment(total_price)
change = payment - total_price

print_receipt(selected_items, total_price, payment, change)
