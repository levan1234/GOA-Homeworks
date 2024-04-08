num = int(input("enter number: "))
num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
num3 = int(input("enter number: "))
num4 = int(input("enter number: "))

my_list = [num,num1,num2,num3,num4]
for i in my_list:
    if i % 2 == 0:
        print(i)
