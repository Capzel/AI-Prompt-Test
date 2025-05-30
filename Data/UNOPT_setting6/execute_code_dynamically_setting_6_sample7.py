def execute_code(code_string):
    exec(code_string)

code_to_execute = """
print('Hello, World!')
x = 5
y = 10
print('Sum:', x + y)
"""

execute_code(code_to_execute)