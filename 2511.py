def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def delenie(num1, num2):
    return num1/num2

def umnogenie(num1,num2):
    return num1*num2

def main():
    operation = input()
        num1 = int(input("Enter value for num1: "))
        num2 = int(input("Enter value for num2: "))
            if (operation == "plus"):
                 print(plus(num1, num2))
            elif (operation == "minus"):
                 print(minus(num1, num2))
            elif (operation == "umnogenie"):
                print(umnogenie(num1,num2))
            elif (operation == "delenie"):
                 print(delenie(num1,num2))

main()