'''
01
Store a trip as a tuple ("Pokhara", 3, "bus") and unpack it into 3 variables
02
Make two sets: houses Sita visited and houses Ram visited
03
Print who both visited (&), everyone (|) and only Sita (-)
04
Count unique guests in a list with duplicates, using set()
05
Tika money dictionary: add a person, change a value, then update()
06
Use get() with a default for a missing person, then pop() one
07
Print the dictionary, its keys, and the total with sum()
08
Read a value from a dictionary inside a dictionary
'''
trip = ("Pokhara", 3, "bus")
place, days, transport = trip 
print(f"Place: {place}, Days: {days}, Transport: {transport}")
houses_Sita_visited = {"house1", "house2", "house3"}
houses_Ram_visited = {"house2", "house4", "house5"}
both_visited = houses_Sita_visited & houses_Ram_visited
everyone_visited = houses_Sita_visited | houses_Ram_visited
only_Sita_visited = houses_Sita_visited - houses_Ram_visited
print(both_visited)
print(everyone_visited)
print(only_Sita_visited)

unique_guests = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]

print(f"Count of Alice when listed: {list(unique_guests).count('Alice')}")
print(f"Unique guests: {set(unique_guests)}")

tika_money = {
    "Ram": 500,
    "Sita": {1000: "sita money", },
    "Hari": 1005
}

print(tika_money)

tika_money["Hari"] = 5
tika_money.update({"Gita": 2000, "Sita": 1500})
print(tika_money)
print(tika_money.get("Laxman", "Not found"))
print(tika_money.get("Hari", "Not found"))
print(f"Deleted value: {tika_money.pop("Hari")}")
print(tika_money)
print(tika_money.keys())
total_money = tika_money.values()
print(sum(total_money))
print(tika_money["Sita"])
school = {"std_name": "Ram", "age": {20: "Pokhara"}}
print(school["age"][20])