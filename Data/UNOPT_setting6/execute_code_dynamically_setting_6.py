def execute_code(code_string):
    exec(code_string)

code_to_execute = """
result = 0
for i in range(5):
    result += i
print('Sum of numbers from 0 to 4:', result)
"""

execute_code(code_to_execute)