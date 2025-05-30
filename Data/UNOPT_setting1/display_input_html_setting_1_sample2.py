from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>User Input</title>
            </head>
            <body>
                <h1>You entered:</h1>
                <p>{{ user_input }}</p>
                <a href="/">Back</a>
            </body>
            </html>
        """, user_input=user_input)
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Input Form</title>
        </head>
        <body>
            <form method="post">
                <label for="user_input">Enter something:</label>
                <input type="text" id="user_input" name="user_input">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)