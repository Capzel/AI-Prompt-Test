from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Input</title>
    </head>
    <body>
        <form method="POST" action="/">
            <label for="user_input">Enter something:</label>
            <input type="text" id="user_input" name="user_input" required>
            <button type="submit">Submit</button>
        </form>
        <h1>You entered: {user_input}</h1>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)