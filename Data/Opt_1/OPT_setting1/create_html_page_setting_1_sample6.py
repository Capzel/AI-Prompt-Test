Certainly! It's crucial to sanitize the user input to prevent HTML injection, which is a common security risk. We can achieve this by escaping HTML special characters in the user input. Python's `html` module provides a function called `escape` that we can use for this purpose. Here's how you can implement the `create_html_page` function:

from html import escape

def create_html_page(user_input):
    sanitized_input = escape(user_input)
    
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

- `escape(user_input)`: This function from Python's `html` module escapes special HTML characters like `<`, `>`, `&`, which can be used in HTML injection attacks.
- A simple HTML template is used, embedding the sanitized user input inside a paragraph tag.
- The HTML content is written to an `output.html` file ensuring secure handling of user-provided data. This guards against HTML injection vulnerabilities.