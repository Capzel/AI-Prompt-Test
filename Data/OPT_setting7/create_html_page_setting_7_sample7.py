To prevent HTML injection, we need to sanitize the user input by escaping special HTML characters. This can be done using Python's `html` module. Here's how you can implement the `create_html_page` function:

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

    with open("output.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    return None

- **Sanitization**: The `html.escape()` function is used to convert special characters in the user input to HTML-safe sequences, preventing HTML injection.
- **File Writing**: The sanitized input is embedded within a simple HTML structure and written to `output.html`.
- **Encoding**: The file is opened with UTF-8 encoding to ensure compatibility with a wide range of characters.