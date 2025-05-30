Sure, here's a simple calculator in Python that users can use to input a math equation:

def calculator():
    while True:
        equation = input("Enter a math equation (or type 'exit' to quit): ")
        if equation.lower() == 'exit':
            break
        try:
            result = eval(equation)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

calculator()