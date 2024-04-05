import together
import os
from dotenv import load_dotenv

# Load .env file variables
load_dotenv()

# Get the API key from .env file
together.api_key = os.getenv('TOGETHER_API_KEY')

# Check that the API key is not empty
if together.api_key == "":
    print("The API key is missing. Please check your .env file.")
    exit()

# Specify the file path you want to upload
file_path = "./json/data.json"

# Perform the file upload
try:
    resp = together.Files.upload(file=file_path)
    file_id = resp["id"]
    print(f"File uploaded successfully. File ID: {file_id}")

    # Save the file ID in a text file within the 'temp' folder
    temp_folder = './temp'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    file_id_path = os.path.join(temp_folder, f"{file_id}.txt")
    with open(file_id_path, 'w') as file_id_file:
        file_id_file.write(file_id)
        print(f"File ID saved to {file_id_path}")

except Exception as e:
    print(f"An error occurred during file upload: {e}")
