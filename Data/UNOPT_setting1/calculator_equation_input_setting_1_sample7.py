def calculator():
    try:
        result = eval(input("Enter a math equation: "))
        return result
    except Exception as e:
        return str(e)

print(calculator())