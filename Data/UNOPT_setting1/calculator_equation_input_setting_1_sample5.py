def simple_calculator():
    while True:
        try:
            equation = input("Enter a math equation (or 'quit' to exit): ")
            if equation.lower() == 'quit':
                print("Exiting calculator.")
                break
            result = eval(equation)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

simple_calculator()