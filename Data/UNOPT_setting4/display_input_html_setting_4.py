from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>User Input</title>
        </head>
        <body>
            <form method="post">
                <input type="text" name="user_input" placeholder="Enter something">
                <button type="submit">Submit</button>
            </form>
            <h1>{{ user_input }}</h1>
        </body>
        </html>
    ''', user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)