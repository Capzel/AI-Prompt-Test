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
    <h1>User Input Form</h1>
    <form method="post">
      <label for="user_input">Enter something:</label>
      <input type="text" id="user_input" name="user_input">
      <input type="submit" value="Submit">
    </form>
    {% if display_input %}
      <h2>User Input:</h2>
      <p>{{ display_input }}</p>
    {% endif %}
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
    return render_template_string(html_template, display_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)