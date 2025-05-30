To create a function `create_html_page(user_input)` that writes sanitized input into an HTML file, we need to ensure that any potentially harmful HTML tags or scripts are neutralized to prevent HTML injection. We can achieve this by escaping special HTML characters. Here's how you can implement this function:

import html

def create_html_page(user_input):
    sanitized_input = html.escape(user_input)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Safe HTML Page</title>
    </head>
    <body>
        <p>{sanitized_input}</p>
    </body>
    </html>
    """

    with open("output.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    return None

- **Sanitization**: We use `html.escape()` to convert special characters like `<`, `>`, `&`, and `"` into their corresponding HTML-safe sequences (`&lt;`, `&gt;`, `&amp;`, `&quot;`).
- **File Handling**: The HTML content is written to `output.html` using a context manager to ensure the file is properly closed after writing.
- **Security**: This approach prevents HTML injection by ensuring that any user input is safely rendered as text, not executable HTML or JavaScript.