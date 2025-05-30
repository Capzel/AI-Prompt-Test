from flask import Flask, render_template_string, request

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input</title>
</head>
<body>
    <form method="POST">
        <label for="user_input">Enter something:</label>
        <input type="text" id="user_input" name="user_input">
        <button type="submit">Submit</button>
    </form>
    <h2>User Input:</h2>
    <p>{{ user_input }}</p>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
    return render_template_string(html_template, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)