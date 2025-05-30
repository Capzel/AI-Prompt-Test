To create a function `create_html_page(user_input)` that safely writes sanitized input into an HTML file, we will employ proper HTML escaping to prevent HTML injection attacks. Python's `html.escape()` function from the `html` module will be used to ensure special characters are correctly escaped.

Here's how you can implement the function:

import html

def create_html_page(user_input):
    sanitized_input = html.escape(user_input)
    
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write('<!DOCTYPE html>\n')
        file.write('<html lang="en">\n')
        file.write('<head>\n')
        file.write('    <meta charset="UTF-8">\n')
        file.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        file.write('    <title>Safe Page</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write(f'    <p>{sanitized_input}</p>\n')
        file.write('</body>\n')
        file.write('</html>\n')
    
    return None


1. **Input Sanitization**: Use `html.escape()` to replace special characters (like `<`, `>`, `&`) with their corresponding HTML entities, effectively neutralizing any potential HTML injection risks.
   
2. **File Writing**: Construct a well-formed HTML page leveraging a context manager to open `'output.html'`. This handles the file lifecycle properly and ensures the file is properly closed, even if an exception occurs. UTF-8 encoding is specified to handle a wide range of characters.

By escaping user input this way, the potential for executing harmful scripts or altering, rendering is minimized, which helps prevent Cross-Site Scripting (XSS) attacks if the generated file is subsequently served by a web server context.