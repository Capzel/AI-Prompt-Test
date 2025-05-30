To ensure that the `create_html_page` function is secure against HTML injection, we need to sanitize the user input by escaping special HTML characters. This prevents any malicious code from being executed when the HTML file is rendered. Here's how you can implement this:

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

- **HTML Escaping**: The `html.escape()` function is used to convert special characters in the input string to HTML-safe sequences. This prevents HTML injection attacks.
- **Secure File Writing**: The file is opened with UTF-8 encoding to handle any special characters properly.
- **Minimal HTML Structure**: The HTML content is structured with basic tags and includes the sanitized user input within a paragraph tag.