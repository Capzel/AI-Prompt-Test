def calculator():
    while True:
        equation = input("Enter a mathematical expression (or 'exit' to quit): ")
        if equation.lower() == 'exit':
            break
        try:
            result = eval(equation)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

calculator()