def calculator():
    while True:
        equation = input("Enter a math equation (or type 'quit' to exit): ")
        if equation.lower() == 'quit':
            break
        try:
            result = eval(equation)
            print(f"Result: {result}")
        except Exception as e:
            print("Invalid equation. Please try again.")

calculator()