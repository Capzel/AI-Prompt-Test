def simple_calculator():
    try:
        equation = input("Enter a math equation: ")
        result = eval(equation)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

simple_calculator()