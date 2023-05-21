#Get Input from Users using input method

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

if(num1 == num2):
    print("{} and {} Both are Equal".format(num1, num2))
elif(num1>num2):
    print("{} is greater than {}".format(num1, num2))
else:
    print("{} is greater than {}".format(num2, num1))