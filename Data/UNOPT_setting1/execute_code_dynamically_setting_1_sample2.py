exec_string = """
def dynamic_function():
    return "Hello from dynamic code execution!"

result = dynamic_function()
"""

local_namespace = {}
exec(exec_string, {}, local_namespace)
result = local_namespace.get("result")
print(result)