import requests
import pandas as pd

# Load the dataset
data = pd.read_csv('dataset_uncoded.csv')
feature_names = data.columns[1:]

# Encode the user preferences
user_preferences = {}
for feature in feature_names:
    user_preferences[feature] = 1

# Send a POST request to the API endpoint
response = requests.post("http://localhost:8000/predict", json={"track": 1})

# Check if the request was successful
if response.status_code == 200:
    # Get the predictions from the response
    predictions = response.json()["predictions"]

    # Print the predictions
    for prediction in predictions:
        print(f"Track: {prediction['track']}, Probability: {prediction['probability']}")
else:
    print("Error:", response.status_code)
