

kites = ["red", "blue", "green"]
kites.append("yellow")
print(f"Yellow added: {kites}")
kites.insert(0, "black")
print(f"Black kite added: {kites}")
kites.remove("green")
print(f"Green Kite removed: {kites}")
sold = kites.pop()
print(f"{sold} kite sold")
kites.sort()
print(f"Sorted kites: {kites}")
print(f"The first two kites: {kites[:2]}")
print(f"Number of kite stock: {len(kites)}, {kites} blue in stock: {"blue" in kites}")

colors = "pink, orange, white"
as_list = colors.split(", ")

print(as_list)
a = set(kites)
b = set(as_list)
union = a | b
print(f"Union of kites and colors: {union}")
gold = union.copy()
gold.add("gold")
print(f"Original kites: {union}, New kites: {gold}")
With_prices = [["small", 50], ["big", 150]]
print(f"Big kite's price: {With_prices[1][1]}")