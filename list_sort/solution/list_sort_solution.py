import json
from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/')
def index():
    """
    Loads the index page.
    """
    return render_template('index.html')


@app.route('/sort', methods=['POST'])
def sort():
    print(request.form)

    results = {}
    results["unsorted"] = request.form['list'].split(",")
    results["order"] = "ASC" if request.form['isASC'] else "DESC"
    results["sorted"] = sorted(results["unsorted"], reverse = False if request.form['isASC'] == 'true' else True)

    results_json = json.dumps(results)
    print(results_json)

    return Response(results_json, status=200, mimetype='application/json')