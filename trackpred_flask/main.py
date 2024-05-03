import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# this should be the same as backend fastapi port
PORT = '80'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get user preferences from the form
    user_preferences = {}
    for key in request.form:
        user_preferences[key] = int(request.form[key])
    print(user_preferences)

    # Send a POST request to the API endpoint
    # be=backend, a network alias we set to the fastapi backend container
    response = requests.post("http://be:%s/predict" % PORT, json=user_preferences)

    if response.status_code == 200:
        # Get the predictions from the response
        predictions = response.json()["predictions"]
        return render_template("result.html", predictions=predictions)
    else:
        return "Error: Failed to fetch predictions", 500

# https://stackoverflow.com/questions/76780688/running-a-flask-app-in-docker-doesnt-show-a-page-in-browser
if __name__ == "__main__":
    app.run()
