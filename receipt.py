
name = input("Enter your name: ").title()
item = input("Enter item name: ").capitalize()
price = float(input("Enter price: "))
quantity = int(input("Enter item quantity: "))

total = round(price * quantity, 2)
divrem = divmod(total, 500)

print(f"{item}, code: {item[:3]}")
print(f"Total price is Rs.{total}")
print(f"Rs. 500 notes: {int(divrem[0])}, Remaining amount: Rs.{divrem[1]}")
print("Is the total over Rs. 1000?", total > 1000)
print("Type of price variable:", type(price))

