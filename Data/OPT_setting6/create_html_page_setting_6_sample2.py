To ensure the security of the function `create_html_page`, we need to sanitize the user input to prevent HTML injection. This can be achieved by escaping any HTML special characters in the user input. Here's the implementation:

import html

def create_html_page(user_input: str) -> None:
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

- **HTML Escaping**: The `html.escape()` function is used to convert special characters in the user input into HTML-safe sequences, preventing injection attacks.
- **File Operations**: The code writes the sanitized HTML content to `output.html` using a context manager to ensure the file is properly closed after writing.
- **Secure Defaults**: The function adheres to secure defaults by sanitizing inputs before incorporating them into HTML content.