
def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            inventory = int(file.readline())
            history = eval(file.readline())

        return inventory, history

    except FileNotFoundError:
        return 0, []

def save_inventory(inventory, history):
    with open("inventory.txt", "w") as file:
        file.write(str(inventory) + "\n")
        file.write(str(history) + "\n")

def get_valid_input():
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock.lower() == "quit":
        return "quit"

    if not stock.isdigit():
        print("Invalid input. Please enter a whole number.")
        return "invalid"

    return int(stock)

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


# Load previously saved inventory
inventory, transaction_history = load_inventory()

failed_entries = 0
deliveries_processed = 0

print("Previous inventory:", inventory)
print("Previous transaction history:", transaction_history)

while True:
    stock = get_valid_input()

    if stock == "quit":
        save_inventory(inventory, transaction_history)
        print("Inventory and transaction history saved.")
        break

    if stock == "invalid":
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)

    transaction_history.append(stock)

    tax = calculate_tax(stock)

    print("Tax for this delivery:", tax)
    print("Current inventory:", inventory)

    deliveries_processed += 1

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        save_inventory(inventory, transaction_history)
        print("Inventory and transaction history saved.")
        break

generate_report(deliveries_processed, failed_entries)