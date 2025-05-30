from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Input Display</title>
    </head>
    <body>
        <form method="POST">
            <input type="text" name="user_input">
            <button type="submit">Submit</button>
        </form>
        <h1>User Input:</h1>
        <p>{{ user_input }}</p>
    </body>
    </html>
    '''
    return render_template_string(html, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)