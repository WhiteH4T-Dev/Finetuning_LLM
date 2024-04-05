import os
from dotenv import load_dotenv
import together

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'  # Reset to default color

# Load .env file variables
load_dotenv()

# Get the API key from .env file
together.api_key = os.getenv('TOGETHER_API_KEY')

# Check that the API key is not empty
if together.api_key == "":
    print(RED + "The API key is missing. Please check your .env file." + ENDC)
    exit()

# Check the file with the API
resp = together.Files.check(file="./json/data.json")

# Check the response and print appropriate message
if resp.get('is_check_passed'):
    print(GREEN + "Dataset looks good to go." + ENDC)
else:
    print(RED + "Dataset is not ready. Here's the issue:" + ENDC, resp)

print(resp)
