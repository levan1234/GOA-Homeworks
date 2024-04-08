num = 2

while num < 20:
    print(num)
    num=num + 2
while True:
    user_num = int(input("please enter positive nums: "))
    if user_num < 0:
        break
print("you fail")
