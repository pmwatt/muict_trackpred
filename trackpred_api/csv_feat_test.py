import csv

csv_file_path = 'dataset_uncoded.csv'  # Path to your CSV file
feature_names = []

with open(csv_file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    feature_names = next(csv_reader)  # Read the first row

print(feature_names)
