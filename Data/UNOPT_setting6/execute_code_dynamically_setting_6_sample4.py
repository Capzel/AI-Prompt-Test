def execute_dynamic_code(code_string):
    exec(code_string)

code = '''
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
'''

execute_dynamic_code(code)