To prevent HTML injection, you should sanitize the user input by escaping special HTML characters. This can be done using Python's built-in `html` module. Here's how you can create the `create_html_page` function:

import html

def create_html_page(user_input):
    sanitized_input = html.escape(user_input)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Page</title>
</head>
<body>
    <p>{sanitized_input}</p>
</body>
</html>"""

    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    return None

- **Sanitization**: The `html.escape` function is used to replace characters like `<`, `>`, `&`, and `"` with their corresponding HTML-safe sequences.
- **HTML Structure**: The sanitized input is inserted into a basic HTML template.
- **File Writing**: The HTML content is then written to `output.html` using UTF-8 encoding to ensure compatibility with a wide range of characters.
- **Return**: The function returns `None` after writing the file.