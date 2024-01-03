# Input two numbers and an operator
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
operator = input("Oprerator (+, -, *, /): ")

# Decision making and calculating result
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not possible.")
    else:
        result = num1 / num2
else:
    print("Invalid operator.")

# Printing result
print(str(num1) + " " + operator + " " + str(num2) + " is: " + str(result))

