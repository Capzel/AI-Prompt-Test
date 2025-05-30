from html import escape

def generate_html(user_input):
    escaped_input = escape(user_input)
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Display User Input</title>
    </head>
    <body>
        <h1>User Input</h1>
        <p>{escaped_input}</p>
    </body>
    </html>
    """
    return html_template

user_input = input("Enter a string: ")
html_content = generate_html(user_input)
print(html_content)