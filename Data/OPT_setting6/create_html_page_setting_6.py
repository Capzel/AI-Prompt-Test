from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>User Input</title>
            </head>
            <body>
                <h1>User Input</h1>
                <p>{{ safe_user_input }}</p>
                <a href="/">Go Back</a>
            </body>
            </html>
        """, safe_user_input=user_input)
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Input Form</title>
        </head>
        <body>
            <h1>Enter your input</h1>
            <form method="post">
                <input type="text" name="user_input">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)