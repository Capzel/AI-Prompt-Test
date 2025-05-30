def calculator():
    equation = input("Enter a math equation: ")
    try:
        result = eval(equation)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

calculator()