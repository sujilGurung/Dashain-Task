for i in range(1, 15 + 1):
    if i == 7:
        print(f"Day {i}: Fulpati!")
        continue
    if i == 10:
        print(f"Day {i}: the tika day!")
        break
    print(f"Day {i}")

amount = 0
while True:
    choice = input("1 Add, 2 Spend, 3 Balance, 4 Quit: ")
    if choice == "1":
        amount += int(input("Enter the amount: "))
    elif choice == "2":
        spend = int(input("Enter the amount: "))
        if spend > amount:
            print("Not enough money!")
            continue
        amount -= spend
    elif choice == "3":
        print(f"Your current balance Rs.{amount}")
    elif choice == "4":
        print("Bye! Happy Dashain.")
        break
    else:
        print("Wrong choice, try again.")