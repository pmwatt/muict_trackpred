import pickle

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import sklearn

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the dataset
data = pd.read_csv("dataset_uncoded.csv")
feature_names = data.columns[1:]  # Exclude the first column (target variable)

# List of class names (track names)
class_names = model.classes_


class UserPreferences(BaseModel):
    html_css_js: int
    scikitlearn: int
    git: int
    powerbi: int
    numpypandas: int
    unity: int
    mysql: int
    blender: int
    arduinoraspberrypi: int
    mongodb: int
    team_role_excitement: int
    game_career_preference: int
    health_app_contribution2: int
    interactive_3d_animations: int
    intelligent_techniques: int
    ml_models: int
    advanced_data_structures: int
    database_project: int
    software_testing: int
    scm_crm_bi_systems: int
    healthcare_standards: int
    lowlevel_3d_graphics: int
    software_project: int
    network_infrastructure2: int
    microcontroller_programming: int
    business_requirements_analysis: int
    efficient_algorithms: int
    system_security_reliability: int
    system_integration: int
    fullstack_web_developer: int
    data_engineer: int
    network_administrator: int
    animator_3d: int
    bi_consultant: int
    healthcare_info_systems: int
    it_project_manager: int
    ml_engineer: int


app = FastAPI()


@app.post("/predict")
def predict(user_preferences: UserPreferences):
    # Convert user preferences to a DataFrame
    data = pd.DataFrame([user_preferences.dict()])
    print(data)

    # Make predictions
    probabilities = model.predict_proba(data.values)[0]

    # Create a list of dictionaries with track names and probabilities
    predictions = [
        {"track": class_names[i], "probability": float(probabilities[i])}
        for i in range(len(class_names))
    ]

    # Return the predictions as a JSON response
    return {"predictions": predictions}
