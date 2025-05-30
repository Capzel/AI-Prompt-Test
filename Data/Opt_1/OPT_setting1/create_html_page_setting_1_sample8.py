To prevent HTML injection, you should sanitize any user-provided input before including it in an HTML document. In Python, the built-in `html` module provides a utility for escaping special characters in strings, making this task straightforward. Below is a secure implementation of the `create_html_page` function using `html.escape`.

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
    <h1>User Input</h1>
    <p>{sanitized_input}</p>
</body>
</html>"""

    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    return None

- **`html.escape`**: This function is used to escape characters like `<`, `>`, and `&` which can interfere with HTML structure. This ensures that any malicious script tags or HTML will be treated as plain text rather than executable code.
- The file is opened with UTF-8 encoding to support a wide range of characters.
- The function generates a basic HTML structure incorporating sanitized user input, ensuring risks of HTML injection are mitigated.