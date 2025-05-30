To prevent HTML injection, we need to sanitize the user's input before writing it to the HTML file. This can be achieved by escaping special HTML characters. Here's a function that accomplishes this:

import html

def create_html_page(user_input):
    sanitized_input = html.escape(user_input)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Output</title>
    </head>
    <body>
        <p>{sanitized_input}</p>
    </body>
    </html>
    """

    with open("output.html", "w") as file:
        file.write(html_content)

    return None

- **Sanitization**: The `html.escape()` function is used to replace special characters like `<`, `>`, `&`, `'`, and `"` with their corresponding HTML-safe sequences (e.g., `&lt;`, `&gt;`, `&amp;`).
- **File Writing**: The sanitized content is embedded within a basic HTML structure and written to `output.html`.
- **Security**: This approach prevents HTML injection by ensuring that any HTML tags or scripts in the `user_input` are safely escaped.