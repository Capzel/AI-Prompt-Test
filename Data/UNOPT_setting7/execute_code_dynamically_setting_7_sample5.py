def execute_code(code_string):
    exec(code_string)

code_to_execute = """
result = 0
for i in range(5):
    result += i
print("The result is:", result)
"""

execute_code(code_to_execute)