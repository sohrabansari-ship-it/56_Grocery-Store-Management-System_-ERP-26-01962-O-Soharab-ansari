# Grocery Store Management System

inventory = {
    "Rice": {"price": 50.0, "stock": 100},
    "Sugar": {"price": 45.0, "stock": 50},
    "Milk": {"price": 30.0, "stock": 40},
    "Oil": {"price": 150.0, "stock": 20}
}


def show_stock():
    print("\n--- Available Stock ---")
    # Matches Test Case 4(b) format cleanly
    stock_line = " | ".join([f"{item}: {inventory[item]['stock']}" for item in inventory])
    print(stock_line)
    print("")


def new_bill():
    cart = []

    print("\n--- Create New Bill ---")
    print("Enter 'done' to finish.")

    while True:
        name = input("Enter item name: ").strip()

        if name.lower() == "done":
            break

        # Check whether the item exists
        found = None
        for item in inventory:
            if item.lower() == name.lower():
                found = item
                break

        if found is None:
            print(f"Item '{name}' not found in inventory.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Please enter a valid quantity.")
                continue
        except ValueError:
            print("Please enter numbers only.")
            continue

        # Check already added quantity in cart + new quantity
        in_cart = sum(item["quantity"] for item in cart if item["name"] == found)
        available = inventory[found]["stock"] - in_cart

        if quantity > available:
            print(f"Insufficient stock for {found}. Available: {available}")
            continue

        cart.append({
            "name": found,
            "price": inventory[found]["price"],
            "quantity": quantity
        })

        print(found, "added to cart successfully.")

    if len(cart) == 0:
        print("No items selected.")
        return

    # Calculate total amount
    subtotal = 0
    for item in cart:
        subtotal += item["price"] * item["quantity"]

    # Apply discount
    if subtotal >= 1000:
        discount = subtotal * 0.10
        discount_text = "Discount (10%)"
    else:
        discount = 0.0
        discount_text = "Discount"

    amount = subtotal - discount

    # Calculate GST
    gst = amount * 0.05
    total = amount + gst

    # Update stock
    for item in cart:
        name = item["name"]
        inventory[name]["stock"] -= item["quantity"]

    # Display bill (exact format from assignment sheet)
    print("\n==== FINAL BILL ====")
    for item in cart:
        cost = item["price"] * item["quantity"]
        print(f"{item['name']} x {item['quantity']} = Rs. {cost:.2f}")

    print("")
    print(f"Subtotal: {subtotal:.2f} | {discount_text}: {discount:.2f}")
    print(f"GST (5%): {gst:.2f} | Total: Rs. {total:.2f}")
    print("")

    # Save bill in a text file
    with open("bills.txt", "a") as file:
        file.write("\n==== NEW BILL ====\n")
        for item in cart:
            cost = item["price"] * item["quantity"]
            file.write(f"{item['name']} x {item['quantity']} = Rs. {cost:.2f}\n")

        file.write(f"Subtotal: {subtotal:.2f} | {discount_text}: {discount:.2f}\n")
        file.write(f"GST (5%): {gst:.2f} | Total: Rs. {total:.2f}\n\n")

    print("Bill saved successfully!")


# program
while True:
    print("\n=== GROCERY STORE MANAGEMENT ===")
    print("1. Create New Bill")
    print("2. View Available Stock")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        new_bill()
    elif choice == "2":
        show_stock()
    elif choice == "3":
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice! Try again.")
        
