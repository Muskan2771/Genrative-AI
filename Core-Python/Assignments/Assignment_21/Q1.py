try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        result = num1 / num2
    else:
        raise ValueError("Invalid Operator")

    print("Result:", result)

except ValueError as ve:
    print("Error:", ve)

except ZeroDivisionError as ze:
    print("Error:", ze)

except Exception:
    print("Error: Invalid number entered")
