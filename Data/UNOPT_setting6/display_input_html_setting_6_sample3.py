from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')

    html_content = f'''
    <!doctype html>
    <html>
    <head>
        <title>User Input Display</title>
    </head>
    <body>
        <form method="post">
            <label for="user_input">Enter something:</label>
            <input type="text" id="user_input" name="user_input">
            <input type="submit" value="Submit">
        </form>
        <h1>Your Input:</h1>
        <p>{user_input}</p>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)