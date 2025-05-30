To prevent HTML injection, it's important to sanitize the user input by escaping any special HTML characters. This will ensure that any potentially malicious scripts or code that the user may include are not executed as HTML or JavaScript.

Here's the implementation of `create_html_page` with security considerations:

import html

def create_html_page(user_input: str) -> None:
    sanitized_input = html.escape(user_input)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input</title>
</head>
<body>
    <h1>User Provided Content</h1>
    <p>{sanitized_input}</p>
</body>
</html>"""

    with open("output.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    return None

- **HTML Escaping**: Uses `html.escape` to convert special HTML characters to their respective HTML-safe sequences.
- **Minimal HTML Structure**: Constructs a basic HTML around sanitized input.
- **Safe File Handling**: Uses `with open` for secure file operations with UTF-8 encoding to handle all character types. 

This function effectively ensures the user input is not interpreted as HTML/JavaScript and writes a safe HTML file.