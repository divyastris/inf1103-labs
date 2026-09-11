inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock.lower() == "quit":
        break

    if not stock.isdigit():
        print("Invalid input. Please enter a whole number.")
        failed_entries += 1
        continue

    stock = int(stock)

    if stock < 0:
        print("Invalid input. Stock cannot be negative.")
        failed_entries += 1
        continue

    inventory += stock
    print("Current inventory:", inventory)