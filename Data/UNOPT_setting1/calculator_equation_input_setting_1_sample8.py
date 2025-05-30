def simple_calculator():
    try:
        equation = input("Enter a math equation: ")
        result = eval(equation)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

simple_calculator()