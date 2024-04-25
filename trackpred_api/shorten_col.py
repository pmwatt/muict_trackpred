import pandas as pd

# Load the CSV file
data = pd.read_csv('dataset_uncoded.csv')

# Shorten the column names
short_column_names = [
    "track", "html_css_js", "scikitlearn", "git", "powerbi", "numpypandas",
    "unity", "mysql", "blender", "arduinoraspberrypi",
    "mongodb", "team_role_excitement",
    "game_career_preference", "health_app_contribution2",
    "interactive_3d_animations", "intelligent_techniques",
    "ml_models", "advanced_data_structures", "database_project",
    "software_testing", "scm_crm_bi_systems", "healthcare_standards",
    "lowlevel_3d_graphics", "software_project", "network_infrastructure2",
    "microcontroller_programming", "business_requirements_analysis", "efficient_algorithms",
    "system_security_reliability", "system_integration", "fullstack_web_developer",
    "data_engineer", "network_administrator", "animator_3d", "bi_consultant",
    "healthcare_info_systems", "it_project_manager", "ml_engineer",
]

data.columns = short_column_names

# Save the updated DataFrame to a new CSV file
data.to_csv('shortened_dataset.csv', index=False)
