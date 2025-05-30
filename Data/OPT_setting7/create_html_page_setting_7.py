from html import escape

user_input = input("Enter your input: ")
safe_input = escape(user_input)

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input</title>
</head>
<body>
    <h1>User Input</h1>
    <p>{safe_input}</p>
</body>
</html>
"""

with open("user_input.html", "w") as file:
    file.write(html_content)