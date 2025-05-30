To prevent HTML injection, we need to sanitize the user input by escaping special HTML characters. This can be achieved using Python's `html` module. Here's how you can implement the `create_html_page` function:

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

    with open("output.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    return None

- **Sanitization**: We use `html.escape()` to convert special characters like `<`, `>`, `&`, etc., into their HTML-safe representations (`&lt;`, `&gt;`, `&amp;`, etc.).
- **File Writing**: The sanitized input is embedded in a basic HTML structure and written to `output.html`.
- **Security**: This approach mitigates the risk of HTML injection by ensuring that any potentially harmful HTML tags or scripts in the user input are neutralized.