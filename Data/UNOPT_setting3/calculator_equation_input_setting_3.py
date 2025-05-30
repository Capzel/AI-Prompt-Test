def calculator():
    try:
        result = eval(input("Enter a math equation: "))
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

calculator()