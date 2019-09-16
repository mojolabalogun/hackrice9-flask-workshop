from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def calculate():
    result = ""
    if request.method == "POST":
        print request.form
        expression = request.form.get('display')
        try:
            print(expression)
            result = eval(expression)
        except Exception as e:
            result = "ERROR: Clear and Try Again!"
            print(e)
    return render_template('index.html', value=result)

if __name__ == "__main__":
    app.run()