
menu = [
    ("buff momo", 180),
    ("veg momo", 150),
    ("chicken momo", 220),
    ("tea", 40)
]

# 01: Calculate total bill with any number of prices
def total_bill(*prices, discount=0):
    total = sum(prices)
    return total - discount


prices = []

for menu_item, price in menu:
    print(f"{menu_item.title()} costs Rs. {price}")
    prices.append(price)

total = total_bill(*prices)
print(f"Total: Rs. {total}")


# 02: Call with 3 prices, discount=40, and *cart
print("Three prices:", total_bill(180, 150, 40))

discounted_total = total_bill(*prices, discount=40)
print(f"Total after discount: Rs. {discounted_total}")

cart = [180, 150, 220]
total_cart = total_bill(*cart)
print(f"Total of cart: Rs. {total_cart}")


# 03: Accept customer, multiple items, and extra details
def make_order(customer, *items, **extras):
    print(f"\nOrder for {customer.title()}:")

    for item in items:
        print(f"- {item.title()}")

    for extra, value in extras.items():
        print(f"{extra.title()}: {value}")


make_order(
    "Ram",
    "veg momo",
    "tea",
    momo="chili",
    napkins=2
)


# 04: Sort the menu by price
sorted_menu = sorted(menu, key=lambda x: x[1])

print("\nSorted menu by price:")
for menu_item, price in sorted_menu:
    print(f"{menu_item.title()} costs Rs. {price}")


# 05: Find the costliest item
costliest_item = max(menu, key=lambda x: x[1])

print(
    f"\nThe costliest item is {costliest_item[0].title()} "
    f"at Rs. {costliest_item[1]}"
)


# 06: Add a 10% service charge using map()
service_charge = list(
    map(lambda x: (x[0], round(x[1] * 1.1, 2)), menu)
)

print("\nMenu with 10% service charge:")
for menu_item, price in service_charge:
    print(f"{menu_item.title()} costs Rs. {price}")


# 07: Keep only items under Rs. 200 using filter()
under_200 = list(filter(lambda x: x[1] < 200, menu))

print("\nItems under Rs. 200:")
for menu_item, price in under_200:
    print(f"{menu_item.title()} costs Rs. {price}")
