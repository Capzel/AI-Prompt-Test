import html

def create_html_page(user_input):
    sanitized_input = html.escape(user_input)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Output Page</title>
    </head>
    <body>
        <p>{sanitized_input}</p>
    </body>
    </html>
    """
    
    with open('output.html', 'w') as file:
        file.write(html_content)
    
    return None

- **Input Sanitization**: The `html.escape` method is used to convert special characters in the user input into HTML-safe sequences, preventing potential HTML injection attacks.
- **Writing HTML File**: The sanitized input is embedded into a basic HTML structure and then written to an `output.html` file.
- **Security**: Escaping user input is crucial as it prevents executing malicious scripts that could be injected through the input.