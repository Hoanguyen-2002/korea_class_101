import os
import json
import sys
def create_folder_and_subfolder(parent_folder, subfolder):
    try:
        # Create the parent folder
        if not os.path.exists(parent_folder):
            os.makedirs(parent_folder)
            print(f"Parent folder '{parent_folder}' created.")
        else:
            print(f"Parent folder '{parent_folder}' already exists.")
        
        # Create the subfolder within the parent folder
        subfolder_path = os.path.join(parent_folder, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            print(f"Subfolder '{subfolder}' created inside '{parent_folder}'.")
        else:
            print(f"Subfolder '{subfolder}' already exists inside '{parent_folder}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
with open('courses.json', 'r') as file:
    # Read the entire file content
    content = file.read()
    datas = json.loads(content)

    # Create folders
    for folder in datas['folders']:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")



