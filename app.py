from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("site/index.html")
@app.route('/categoria')
def animais():
    return render_template("site/animais.html")

app.run(debug=True)