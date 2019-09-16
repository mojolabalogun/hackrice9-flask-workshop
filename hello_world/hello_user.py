from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello(user):
    return "Hello, World!"

@app.route("/<user>")
def hello_user(user):
    return "Hello, %s!" % user

if __name__ == "__main__":
    app.run()
