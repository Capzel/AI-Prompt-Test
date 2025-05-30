def execute_code(code_string):
    exec(code_string)

code_to_execute = """
def greet(name):
    return f'Hello, {name}!'

print(greet('World'))
"""

execute_code(code_to_execute)