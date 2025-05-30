To prevent HTML injection, we need to sanitize the user input by escaping special HTML characters. This can be done using Python's `html` module, which provides a function `escape()` to convert special characters to HTML-safe sequences. Here's how you can implement the `create_html_page` function:

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
        <h1>User Input</h1>
        <p>{sanitized_input}</p>
    </body>
    </html>
    """

    with open("output.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    return None


- **Sanitization**: The `html.escape()` function is used to replace characters like `<`, `>`, `&`, and `"` with their corresponding HTML-safe sequences (`&lt;`, `&gt;`, `&amp;`, `&quot;`), effectively neutralizing any potential HTML or script injection.
- **HTML Structure**: A basic HTML structure is defined, and the sanitized user input is inserted into the `<p>` tag.
- **File Writing**: The sanitized HTML content is written to `output.html` using UTF-8 encoding to ensure compatibility with a wide range of characters.