from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user preferences from the form
    user_preferences = {}
    for key in request.form:
        user_preferences[key] = int(request.form[key])
    print(user_preferences)

    # Send a POST request to the API endpoint
    response = requests.post("http://localhost:8000/predict", json=user_preferences)

    if response.status_code == 200:
        # Get the predictions from the response
        predictions = response.json()["predictions"]
        return render_template('result.html', predictions=predictions)
    else:
        return "Error: Failed to fetch predictions", 500

if __name__ == '__main__':
    app.run(debug=True)
