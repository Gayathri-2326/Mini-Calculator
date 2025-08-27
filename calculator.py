# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error (division by zero)" if y == 0 else x / y

print("Mini Calculator")
print("Operations: +  -  *  /")

while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+ - * /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            print("Result:", add(num1, num2))
        elif op == '-':
            print("Result:", subtract(num1, num2))
        elif op == '*':
            print("Result:", multiply(num1, num2))
        elif op == '/':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operator")

    except ValueError:
        print("Invalid input, try again.")

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break
