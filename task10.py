
menu = {
    "momo": 180,
    "chowmein": 150,
    "sel roti": 30,
    "tea": 40
}


def ask_quantity(food):
    while True:
        try:
            quantity = int(input(f"Enter quantity for {food}: "))

            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")

        except ValueError as e:
            print(f"Invalid quantity: {e}")
            continue

        else:
            return quantity


def print_bill(cart):
    print("\n========== FINAL BILL ==========")

    total = 0

    for food, quantity in cart.items():
        price = menu[food]
        item_total = price * quantity

        print(f"{food} x {quantity} = Rs. {item_total}")

        total += item_total

    print("--------------------------------")
    print(f"Total bill: Rs. {total}")
    print("================================")


cart = {}

while True:
    food = input("\nEnter food (or 'done' to finish): ").strip().lower()

    if food == "done":
        break

    if food == "":
        print("Please enter a food item.")
        continue

    try:
        price = menu[food]

    except KeyError:
        print(f"Sorry, {food} is not available in the menu.")

    else:
        quantity = ask_quantity(food)

        cart[food] = cart.get(food, 0) + quantity

    finally:
        print("------------------------------")

print_bill(cart)
print("Thank you for visiting our Dashain food shop!")
