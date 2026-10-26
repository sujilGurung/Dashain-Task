'''Banner, countdown and token machine
One small piece of code for each of the three Day 14 tools.

01
Decorator dashain_banner prints a line before and after any function
02
Decorate greet(name, gift="tika") with @ and call it twice
03
Recursive countdown(n): prints days left, then Tika day! at 0
04
Recursive sum_digits(n): sum_digits(2026) gives 10
05
Generator token_machine(start) yields T-101, T-102 ... forever
06
Get 3 tokens with next(). Sum 1² to 5² with a one-line generator'''



def Decorate_greet(name, gift="tika"):
    def wrapper():
        print("***Happy Dashain***")
        result = name()
        print(f"{result} gets {gift}")
        print("*" * 20)
        return result

    return wrapper

@Decorate_greet
def festival():
    name = "Sita"
    return name

@Decorate_greet
def person():
    name = "Hari"
    return name

festival()
person()
print("\n")
def countdown(n):
    if n == 0:
        print("Tika day!")
    else:
        print(n, "days left")
        countdown(n - 1)

countdown(5)

print("\n")
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

print(f"The recursive sum:{sum_digits(2026)}")

print("\n")
def token_machine(start):
    while True:
        yield f"T-{start}"
        start += 1

tokens = token_machine(101)

print(next(tokens))
print(next(tokens))
print(next(tokens))

total = sum(x**2 for x in range(1, 6))
print(total)