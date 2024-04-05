import together
import os
from dotenv import load_dotenv
import glob

# Load .env file variables
load_dotenv()

# Get the API keys from .env file
together_api_key = os.getenv('TOGETHER_API_KEY')
wandb_api_key = os.getenv('WANDB_API_KEY')

# Check that the API keys are not empty
if not together_api_key or not wandb_api_key:
    print("One or more API keys are missing. Please check your .env file.")
    exit()

together.api_key = together_api_key

# Retrieve the file ID from the temp folder
temp_folder = './temp'
file_list = glob.glob(os.path.join(temp_folder, '*.txt'))
if not file_list:
    print("No training file ID found in the temp folder.")
    exit()
with open(file_list[0], 'r') as file_id_file:
    training_file_id = file_id_file.read().strip()

# Start the fine-tuning process with the retrieved file ID
resp = together.Finetune.create(
    training_file=training_file_id,
    model='teknium/OpenHermes-2p5-Mistral-7B',
    n_epochs=3,
    n_checkpoints=1,
    batch_size=4,
    learning_rate=1e-5,
    suffix='CyberShield',
    wandb_api_key=wandb_api_key,
)

fine_tune_id = resp['id']
print(resp)
