To prevent HTML injection, we need to sanitize the user input by escaping special HTML characters. This can be achieved using Python's built-in `html` module. Here's how you can implement the `create_html_page` function:

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

- **Sanitization**: The `html.escape()` function is used to replace special characters like `<`, `>`, `&`, etc., with their corresponding HTML-safe sequences.
- **File Handling**: The HTML content is written to `output.html` using a context manager to ensure the file is properly closed after writing.
- **Security**: This approach mitigates the risk of HTML injection by ensuring that any potentially harmful HTML tags or scripts are rendered harmless.