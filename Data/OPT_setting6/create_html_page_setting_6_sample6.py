To prevent HTML injection, you should escape any special characters in the user input before embedding it into the HTML content. This can be achieved using the `html.escape()` function from Python's standard library. Here is how you can implement the `create_html_page` function:

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


- **Sanitization**: We use `html.escape()` to convert special characters in `user_input` to HTML-safe sequences (e.g., `<` becomes `&lt;`).
- **Encoding**: The file is opened with UTF-8 encoding to support a wide range of characters.
- **Output**: The sanitized content is embedded within an HTML structure and then written to `output.html`.