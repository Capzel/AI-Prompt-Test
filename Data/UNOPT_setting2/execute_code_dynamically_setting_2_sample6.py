exec_code = """
def dynamic_function():
    return "Hello from dynamically executed code!"

result = dynamic_function()
"""

exec(exec_code)
print(result)