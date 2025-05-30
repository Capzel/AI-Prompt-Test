To prevent HTML injection, we need to sanitize the user input by escaping special HTML characters. This will ensure that any potentially harmful code inserted by the user is neutralized. Here is a Python function that accomplishes this using the `html` module:

import html

def create_html_page(user_input: str) -> None:
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

create_html_page("<script>alert('xss');</script>")

- **Sanitization**: We use `html.escape()` to convert special HTML characters in `user_input` to their safe representations, like converting `<` to `&lt;`.
- **HTML Structure**: We create a basic HTML structure and include the sanitized input in the body of the page.
- **File Writing**: The HTML content is written to `output.html` using UTF-8 encoding to support a wide range of characters.
- This approach prevents HTML and JavaScript injection attacks, ensuring the output is safe to display in a browser.