import pandas as pd

# Load the CSV file
data = pd.read_csv("dataset_v4b.csv")

# Shorten the column names
short_column_names = [ "track", # this one is a must-keep, for training as y
    "scikitlearn",
    "powerbi",
    "unity",
    "mysql",
    "blender",
    "mongodb",
    "team_role_excitement",
    "interactive_3d_animations",
    "intelligent_techniques",
    "ml_models",
    "database_project",
    "software_testing",
    "scm_crm_bi_systems",
    "lowlevel_3d_graphics",
    "software_project",
    "business_requirements_analysis",
    "efficient_algorithms",
    "system_integration",
    "fullstack_web_developer",
    "data_engineer",
    "animator_3d",
    "bi_consultant",
    "it_project_manager",
    "ml_engineer",
]

data.columns = short_column_names

# Save the updated DataFrame to a new CSV file
data.to_csv("shortened_dataset.csv", index=False)
