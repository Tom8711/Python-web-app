from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hoi, World!</p>"


@app.route("/tweede/<naam>")
def hello_world2(naam):
    return f"<p>Hello {naam}, tweede!</p>"