from flask import Flask

app = Flask(__name__)

@app.route("/<user>")
def hello(user):
    return "Hello, %s!" % user

if __name__ == "__main__":
    app.run()
