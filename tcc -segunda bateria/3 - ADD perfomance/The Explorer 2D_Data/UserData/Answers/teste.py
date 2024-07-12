import os
import json
import csv

# Specify the path to your main folder
main_folder = 'D:/Users/tubra/Desktop/criacoes/tcc -segunda bateria/3 - ADD perfomance/The Explorer 2D_Data/UserData/Data'

# Specify the path to your output CSV file
output_csv = 'output.csv'

data = []

for folder_name in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder_name)

    # Check if the item in the folder is a directory
    if os.path.isdir(folder_path):
        # Look for survey JSON files in each folder
        json_files = [file_name for file_name in os.listdir(folder_path) if file_name.endswith('.json')]
        row_data = {'user': int(json_files[0].split("-")[0])+1}
        
        for i, fp in enumerate(json_files):
        # Proceed only if there is at least one JSON file in the subfolder
            if json_files:
                file_path = os.path.join(folder_path, fp)

                with open(file_path) as json_file:
                    json_data = json.load(json_file)
                    survey_data = json_data.get('Level - '+str(int(fp.split("-")[1].split("_")[0])+1))
                    print(json_data)
                    print(survey_data)
                    DeathRate = survey_data.get('DeathRate').get('value')

                    # Create a dictionary to store the data for each row


                        # Add question name and answer to the row data
                    row_data[int(fp.split("-")[1].split("_")[0])+1] = DeathRate

                    # Add the row data to the list
        data.append(row_data)

# Get all unique question names from the data
question_names = set([i for i in range(1,12)])


# Write the data to the CSV file
with open(output_csv, 'w', newline='') as csv_file:
    fieldnames = ['user'] + sorted(question_names)
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


print("CSV file created successfully!")