To prevent HTML injection, we need to sanitize the user input by escaping special HTML characters. This can be achieved using Python's `html` module, which provides a function `escape()` to convert special characters to HTML-safe sequences. Here's how you can implement the `create_html_page` function:

import html

def create_html_page(user_input):
    safe_input = html.escape(user_input)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Safe HTML Page</title>
    </head>
    <body>
        <p>{safe_input}</p>
    </body>
    </html>
    """

    with open("output.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    return None

- **Sanitization**: The `html.escape()` function is used to convert special characters like `<`, `>`, `&`, and `"` into their corresponding HTML-safe sequences.
- **File Handling**: The HTML content is written to `output.html` using a context manager (`with` statement) to ensure the file is properly closed after writing.
- **Security**: By escaping user input, we mitigate the risk of HTML injection, ensuring that any HTML tags in the input are treated as plain text rather than executable code.