# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

continueFlag = True

def Calculator():
    continueFlag = True
    while continueFlag:
        Main_Menu()


def Subtraction(num1, num2):
    return int(num1) - int(num2)

def Addition(num1, num2):
    return int(num1) + int(num2)

def Multiplication(num1, num2):
    return int(num1) * int(num2)

def Division(num1, num2):
    return int(num1) / int(num2)

def Modulus(num1, num2):
    return int(num1) % int(num2)

def Main_Menu():
    global continueFlag
    validInputs = ["+", "-", "/", "*", "%", "q", "Q"]
    print("Welcome to Chambies' Calculator Main Menu!\nPlease make a selection below:\n"
          "______________________________")
    print("'+' for Addition\n'-' for Subtraction\n'*' for Multiplication\n'/' for Division\n"
          "'%' for Modulus\n 'Q' for exiting program")
    operator = input("Chosen Operator: ")
    if operator not in validInputs:
        print("Invalid input, Try again... \n")
    else:
        match operator:
            case "q":
                print("Exiting...")
                continueFlag = False
                quit()
            case "Q":
                print("Exiting...")
                continueFlag = False
                quit()

        num1 = input("Your first number: ")
        num2 = input("Your second number: ")

        match operator:
            case "+":
                print("Result: ", Addition(num1, num2))
                time.sleep(3)
                print("Returning to menu...\n\n")
                time.sleep(2)
            case "-":
                print("Result: ", Subtraction(num1, num2))
                time.sleep(3)
                print("Returning to menu...\n\n")
                time.sleep(2)
            case "*":
                print("Result: ", Multiplication(num1, num2))
                time.sleep(3)
                print("Returning to menu...\n\n")
                time.sleep(2)
            case "/":
                if num2 == '0':
                    print("Can't divide by 0, Try again...")
                    time.sleep(1)
                    print("Returning to menu...\n\n")
                    time.sleep(2)
                else:
                    print("Result: ", Division(num1, num2))
                    time.sleep(3)
                    print("Returning to menu...\n\n")
                    time.sleep(2)
            case "%":
                print("Result: ", Modulus(num1, num2))
                time.sleep(3)
                print("Returning to menu...\n\n")
                time.sleep(2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Calculator()

