import os
import json
import csv

# Specify the path to your main folder
main_folder = 'D:/Users/tubra/Desktop/Nova pasta'

# Specify the path to your output CSV file
output_csv = 'output.csv'

# Initialize a list to store the data
data = []

# Iterate over each folder in the main folder
for folder_name in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder_name)

    # Check if the item in the folder is a directory
    if os.path.isdir(folder_path):
        # Look for survey JSON files in each folder
        json_files = [file_name for file_name in os.listdir(folder_path) if file_name.endswith('.json')]

        # Proceed only if there is at least one JSON file in the subfolder
        if json_files:
            file_path = os.path.join(folder_path, json_files[0])

            with open(file_path) as json_file:
                json_data = json.load(json_file)
                survey_data = json_data.get('survey')
                user = survey_data.get('user')
                questions = survey_data.get('questions')

                # Sort the questions based on 'id'
                sorted_questions = sorted(questions, key=lambda q: q['ID'])

                # Create a dictionary to store the data for each row
                row_data = {'user': user}

                # Extract question names and answers
                for question in sorted_questions:
                    question_name = question['Question']
                    answer = question['Answer']

                    # Add question name and answer to the row data
                    row_data[question_name] = answer

                # Add the row data to the list
                data.append(row_data)

# Get all unique question names from the data
question_names = set()
for row in data:
    question_names.update(row.keys())

# Write the data to the CSV file
with open(output_csv, 'w', newline='') as csv_file:
    fieldnames = ['user'] + sorted(question_names)
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("CSV file created successfully!")