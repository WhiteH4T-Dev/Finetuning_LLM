import together
import os
from dotenv import load_dotenv

# Load .env file variables
load_dotenv()

# Get the API key from .env file
together_api_key = os.getenv('TOGETHER_API_KEY')
wandb_api_key = os.getenv('WANDB_API_KEY')

# Check that the API keys are not empty
if not together_api_key or not wandb_api_key:
    print("One or more API keys are missing. Please check your .env file.")
    exit()

together.api_key = together_api_key

resp = together.Finetune.create(
    training_file='file-4d319f52-c3e2-46f2-aa1c-a1b5cf5f3881',
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
