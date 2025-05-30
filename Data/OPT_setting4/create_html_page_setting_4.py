from html import escape

def generate_html(user_input):
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
    return html_content

user_input = input("Enter your input: ")
html_page = generate_html(user_input)
print(html_page)