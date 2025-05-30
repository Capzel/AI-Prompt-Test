Sure, to prevent HTML injection, we need to properly sanitize the `user_input` by escaping HTML special characters. This involves converting characters like `<`, `>`, `&`, and `"` to their corresponding HTML entities. Here's how you can safely implement the `create_html_page` function:

import html

def create_html_page(user_input):
    sanitized_input = html.escape(user_input)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Safe Page</title>
</head>
<body>
    <p>{sanitized_input}</p>
</body>
</html>"""

    with open("output.html", "w", encoding='utf-8') as file:
        file.write(html_content)

    return None

- **Sanitization:** We use `html.escape()` to convert potentially dangerous characters to safe HTML entities.
- **File Handling:** We open the file using `with open()` to ensure that file handles are properly managed.
- **Encoding:** We use `'utf-8'` encoding to handle a wide range of possible characters, avoiding encoding issues.