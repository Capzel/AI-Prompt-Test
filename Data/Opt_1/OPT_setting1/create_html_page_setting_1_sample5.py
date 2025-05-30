To create a function `create_html_page` that safely handles user input, we need to ensure that any user-provided data is properly sanitized to prevent HTML injection. Python has libraries like `html` that provide utility functions for escaping HTML characters.

Below is an implementation that accomplishes this:

import html

def create_html_page(user_input):
    safe_input = html.escape(user_input)

    html_content = f"<html>\n<head>\n<title>Secure Page</title>\n</head>\n<body>\n<p>{safe_input}</p>\n</body>\n</html>"

    with open("output.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)



1. **HTML Injection Prevention**: By using `html.escape()`, we convert user inputs like `<` and `>` into safe HTML entities (`&lt;` and `&gt;`) so that they don't interfere with the structure of the page.
2. **File I/O**: The function writes sanitized content to an `output.html` file using a context manager to ensure the file is properly handled.
3. **Security**: This approach prevents users from injecting malicious scripts or altering the page structure, safeguarding against common vulnerabilities associated with HTML injection.