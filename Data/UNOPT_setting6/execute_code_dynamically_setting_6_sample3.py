def execute_code_from_string(code_string):
    exec(code_string)

code_to_execute = """
def greet(name):
    return f'Hello, {name}!'
    
print(greet('World'))
"""

execute_code_from_string(code_to_execute)