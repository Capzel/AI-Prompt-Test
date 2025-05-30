from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
    return render_template_string('''
        <html>
            <body>
                <form method="post">
                    <input type="text" name="user_input" placeholder="Enter something">
                    <input type="submit" value="Submit">
                </form>
                <p>{{ user_input }}</p>
            </body>
        </html>
    ''', user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)