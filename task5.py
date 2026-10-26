while True:
    name = input("Enter your name: ").strip()
    if name == "":
        print("Please enter your name.")
    else:
        break

age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
coupon = input("Enter code: ").lower().replace(" ", "")

if age < 5 or height < 110:
    print("Not safe to ride")
else:
    if age >= 60:
        price = 0
    elif age < 12:
        price = 50
    else:
        price = 100

    if price > 0 and coupon in ("dashain", "tihar"):
        price -= 20
        print("Coupon used! Rs 20 off.")

    print(f"{name}, your final price is Rs {price}")