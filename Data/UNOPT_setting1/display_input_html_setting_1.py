from flask import Flask, render_template_string, request

app = Flask(__name__)

html_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>User Input Display</title>
  </head>
  <body>
    <h1>Enter Your Input</h1>
    <form method="POST" action="/">
      <input type="text" name="user_input" required>
      <input type="submit" value="Submit">
    </form>
    {% if user_input %}
    <h2>You entered:</h2>
    <p>{{ user_input }}</p>
    {% endif %}
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def display_input():
    user_input = None
    if request.method == 'POST':
        user_input = request.form['user_input']
    return render_template_string(html_template, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)