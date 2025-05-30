Here is the function `create_html_page` that writes sanitized user input into an HTML file named `output.html`. The function ensures that special characters are escaped to prevent HTML injection:

import html

def create_html_page(user_input: str) -> None:
    sanitized_input = html.escape(user_input)
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Secure Page</title>
</head>
<body>
    <p>{sanitized_input}</p>
</body>
</html>"""

    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    return None

user_input = "Hello, World! <script>alert('XSS');</script>"
create_html_page(user_input)

- The `html.escape()` function is used to convert special characters like `<`, `>`, and `&` to their HTML-safe representations, thereby preventing any potential HTML injections or XSS attacks.
- Error handling mechanisms such as encoding inputs properly are considered, using UTF-8 encoding when writing to preserve input integrity.
- A well-formed basic HTML structure is created, and the sanitized input is inserted between a paragraph tag.