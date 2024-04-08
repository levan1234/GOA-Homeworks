age = int(input("Please enter your age: "))

if age < 18:
    print("You are child")
elif age >= 18 and age < 65:
    print("You are adult")
else:
    print("You are old")
for i in range(5):
    number = int(input("Please enter number: "))

    if number % 2 == 0:
        print(number,"is even")
    else:
        print(number,"is odd")

grade = input("Please enter grade (A,B,C,D or F): ")

if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Good job!")
elif grade == "C":
    print("You passed.")
elif grade == "D":
    print("You can do better.")
else:
    print("You failed.")