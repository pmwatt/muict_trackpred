import pandas as pd

# Load the CSV file
data = pd.read_csv('dataset_uncoded.csv')

# Shorten the column names
short_column_names = [
    "track", "html_css_js", "scikitlearn", "git", "odoo", "powerbi", "numpypandas",
    "cisco_packet_tracer", "unity", "mysql", "blender", "arduinoraspberrypi",
    "mongodb", "large_dataset_appeal", "health_app_contribution", "team_role_excitement",
    "game_career_preference", "health_app_contribution2", "preferred_concepts",
    "interactive_3d_animations", "network_infrastructure", "intelligent_techniques",
    "ecommerce_and_bi", "ml_models", "advanced_data_structures", "database_project",
    "software_testing", "scm_crm_bi_systems", "healthcare_standards",
    "lowlevel_3d_graphics", "software_project", "network_infrastructure2",
    "microcontroller_programming", "business_requirements_analysis", "efficient_algorithms",
    "system_security_reliability", "system_integration", "fullstack_web_developer",
    "data_engineer", "network_administrator", "animator_3d", "bi_consultant",
    "healthcare_info_systems", "it_project_manager", "ml_engineer", "track_rank1",
    "track_rank2", "track_rank3", "track_rank4", "track_rank5", "track_rank6",
    "track_rank7", "track_rank8", "subj_rank1", "subj_rank2", "subj_rank3",
    "subj_rank4", "subj_rank5", "subj_rank6", "subj_rank7", "subj_rank8"
]

data.columns = short_column_names

# Save the updated DataFrame to a new CSV file
data.to_csv('shortened_dataset.csv', index=False)
