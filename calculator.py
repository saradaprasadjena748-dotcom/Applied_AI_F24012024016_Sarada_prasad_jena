a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

choose = input("Enter operator (+, -, *, /): ")

if choose == "+":
    result = a + b
    print("The result is", result)

elif choose == "-":
    result = a - b
    print("The result is", result)

elif choose == "*":
    result = a * b
    print("The result is", result)

elif choose == "/":
    if b != 0:
        result = a / b
        print("The result is", result)
    else:
        print("Division by zero is not allowed")

else:
    print("Invalid operator entered")
