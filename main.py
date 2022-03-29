# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Calculator():

    # numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # operators = ["-", "+", "/", "x", "X", "%", "*", "^"]
    operandOne = int(input("Enter first operand: "))
    operator = input("What Operator? (ex. +, -, *, /, %): ")
    operandTwo = int(input("Enter second operand: "))

    match operator:
        case "-":
            total = operandOne - operandTwo
            print("Result: ", total)
        case "+":
            total = operandOne + operandTwo
            print("Result: ", total)
        case "/":
            if operandTwo == 0:
                print("Can't divide by zero. Try again.")
                exit(Calculator())
            else:
                total = operandOne / operandTwo
                print("Result: ", total)
        case "*":
            total = operandOne * operandTwo
            print("Result: ", total)
        case "%":
            total = operandOne % operandTwo
            print("Result: ", total)


def Main():
    flag = True
    while flag:
        Calculator()
        repeat = input("Would you like to perform another operation? (y or n):  ")
        if repeat == "n":
            flag = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Main()

