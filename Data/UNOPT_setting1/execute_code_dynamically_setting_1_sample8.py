def execute_code(code_string):
    exec(code_string)

sample_code = '''
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
'''

execute_code(sample_code)