from flask import Flask, request
from caesar import rotate_string

form="""<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            p.error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input id="rot" type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>"""

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = request.form['rot']
    rot=int(rot)
    rotated_string = rotate_string(text, rot)
    return form.format(rotated_string)

app.run()