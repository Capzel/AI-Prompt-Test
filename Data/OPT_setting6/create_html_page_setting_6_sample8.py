To ensure the `create_html_page` function is secure against HTML injection, we need to sanitize the user input. We'll use Python's `html` module to escape any potentially harmful characters. Here is the implementation:

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

- **Sanitization**: The `html.escape` method is used to convert special characters like `<`, `>`, and `&` to their corresponding HTML-safe sequences (`&lt;`, `&gt;`, `&amp;`), effectively preventing HTML injection.
- **Encoding**: The file is opened with UTF-8 encoding to ensure compatibility with a wide range of characters.
- **Security**: By escaping user input, we mitigate the risk of injecting malicious scripts or HTML into the page.