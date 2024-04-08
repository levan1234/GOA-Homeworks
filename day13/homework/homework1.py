age = int(input("Please enter your age: "))

if age < 18:
    print("You are child")
elif age >= 18 and age < 65:
    print("You are adult")
else:
    print("You are old")