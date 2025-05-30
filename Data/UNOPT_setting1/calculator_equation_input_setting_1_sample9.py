def simple_calculator(equation):
    try:
        result = eval(equation)
        return result
    except Exception as e:
        return str(e)

user_input = input("Enter a math equation: ")
print(simple_calculator(user_input))