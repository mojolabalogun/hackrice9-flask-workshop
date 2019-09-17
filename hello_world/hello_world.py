from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<b>Hello, World!</b>"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
