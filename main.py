from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST"])
def encrypt():
    rot = (int(request.form['rot']))
    text = request.form['text']
    return "<h1>" + rotate_string(text, rot) + "</h1>"

form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form name="" action="" method="POST">
        <label for="rotate">Rotate by:</label>
            <input name="rot" type="text" id='rotate' value='0' />
            <input name="text" type="textarea" />
            <input type="submit" />
      <!-- create your form here -->
</body>
</html>
"""

@app.route("/")
def index():
    return form

app.run()