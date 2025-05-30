from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
    return render_template_string('''
        <!doctype html>
        <html>
        <head>
            <title>User Input</title>
        </head>
        <body>
            <form method="post">
                <label for="user_input">Enter something:</label>
                <input type="text" id="user_input" name="user_input">
                <input type="submit" value="Submit">
            </form>
            <h1>Your input:</h1>
            <p>{{ user_input }}</p>
        </body>
        </html>
    ''', user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)