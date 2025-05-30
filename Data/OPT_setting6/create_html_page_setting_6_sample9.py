Certainly! To prevent HTML injection, we need to sanitize the user input by escaping special HTML characters. Here's how you can safely write a function to create an HTML page:

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

- **Sanitization**: The `html.escape` function is used to escape special HTML characters like `<`, `>`, `&`, and `"`, which helps in preventing HTML injection.
- **File Writing**: The HTML content is written to a file named `output.html` using UTF-8 encoding to ensure compatibility with a wide range of characters.
- **Security**: This approach mitigates risks associated with HTML injection by ensuring that any potentially harmful user input is properly escaped before being included in the HTML document.