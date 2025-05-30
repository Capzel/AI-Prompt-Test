To safely write user input into an HTML file while preventing HTML injection, you should sanitize the input by escaping special HTML characters. This can be done using Python's `html` module. Here's how you can implement the `create_html_page` function:

import html

def create_html_page(user_input):
    sanitized_input = html.escape(user_input)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Secure Page</title>
    </head>
    <body>
        <p>{sanitized_input}</p>
    </body>
    </html>
    """

    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    return None

- **Sanitization**: The `html.escape()` function is used to convert special characters in the user input to HTML-safe sequences (e.g., `<` becomes `&lt;`).
- **File Writing**: The HTML content is written to `output.html` using UTF-8 encoding to ensure compatibility with various characters.
- **Security**: By escaping user input, we prevent potential HTML injection attacks, ensuring that any HTML tags in the input are treated as plain text.