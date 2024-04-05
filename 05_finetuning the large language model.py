import os
import subprocess
import glob
from dotenv import load_dotenv
import together

# Define clear function based on operating system
def clear_screen():
    if os.name == 'posix':  # For Unix and Linux
        subprocess.run('clear')
    else:  # For Windows
        subprocess.run('cls', shell=True)

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'  # Reset to default color

# Load .env file variables
load_dotenv()

# Get the API keys from .env file
together_api_key = os.getenv('TOGETHER_API_KEY')
wandb_api_key = os.getenv('WANDB_API_KEY')

# Check that the API keys are not empty
if not together_api_key or not wandb_api_key:
    print(RED + "One or more API keys are missing. Please check your .env file." + ENDC)
    exit()

together.api_key = together_api_key

# Ask user for a custom suffix for their model
suffix = input("What do you want to call your model? ")

# Clear the screen
clear_screen()

# Specify the models available
models = {
    "1": "zero-one-ai/Yi-34B-Chat",
    "2": "allenai/OLMo-7B-Instruct",
    "3": "allenai/OLMo-7B-Twin-2T",
    "4": "allenai/OLMo-7B",
    "5": "Austism/chronos-hermes-13b",
    "6": "cognitivecomputations/dolphin-2.5-mixtral-8x7b",
    "7": "deepseek-ai/deepseek-coder-33b-instruct",
    "8": "deepseek-ai/deepseek-llm-67b-chat",
    "9": "garage-bAInd/Platypus2-70B-instruct",
    "10": "google/gemma-2b-it",
    "11": "google/gemma-7b-it",
    "12": "Gryphe/MythoMax-L2-13b",
    "13": "lmsys/vicuna-13b-v1.5",
    "14": "lmsys/vicuna-7b-v1.5",
    "15": "codellama/CodeLlama-13b-Instruct-hf",
    "16": "codellama/CodeLlama-34b-Instruct-hf",
    "17": "codellama/CodeLlama-70b-Instruct-hf",
    "18": "codellama/CodeLlama-7b-Instruct-hf",
    "19": "meta-llama/Llama-2-70b-chat-hf",
    "20": "meta-llama/Llama-2-13b-chat-hf",
    "21": "meta-llama/Llama-2-7b-chat-hf",
    "22": "mistralai/Mistral-7B-Instruct-v0.1",
    "23": "mistralai/Mistral-7B-Instruct-v0.2",
    "24": "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "25": "NousResearch/Nous-Capybara-7B-V1p9",
    "26": "NousResearch/Nous-Hermes-2-Mistral-7B-DPO",
    "27": "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
    "28": "NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT",
    "29": "NousResearch/Nous-Hermes-llama-2-7b",
    "30": "NousResearch/Nous-Hermes-Llama2-13b",
    "31": "NousResearch/Nous-Hermes-2-Yi-34B",
    "32": "openchat/openchat-3.5-1210",
    "33": "Open-Orca/Mistral-7B-OpenOrca",
    "34": "Qwen/Qwen1.5-0.5B-Chat",
    "35": "Qwen/Qwen1.5-1.8B-Chat",
    "36": "Qwen/Qwen1.5-4B-Chat",
    "37": "Qwen/Qwen1.5-7B-Chat",
    "38": "Qwen/Qwen1.5-14B-Chat",
    "39": "Qwen/Qwen1.5-72B-Chat",
    "40": "snorkelai/Snorkel-Mistral-PairRM-DPO",
    "41": "togethercomputer/alpaca-7b",
    "42": "teknium/OpenHermes-2-Mistral-7B",
    "43": "teknium/OpenHermes-2p5-Mistral-7B",
    "44": "togethercomputer/Llama-2-7B-32K-Instruct",
    "45": "togethercomputer/RedPajama-INCITE-Chat-3B-v1",
    "46": "togethercomputer/RedPajama-INCITE-7B-Chat",
    "47": "togethercomputer/StripedHyena-Nous-7B",
    "48": "Undi95/ReMM-SLERP-L2-13B",
    "49": "Undi95/Toppy-M-7B",
    "50": "WizardLM/WizardLM-13B-V1.2",
    "51": "upstage/SOLAR-10.7B-Instruct-v1.0",
    "52": "zero-one-ai/Yi-34B",
    "53": "zero-one-ai/Yi-6B",
    "54": "google/gemma-2b",
    "55": "google/gemma-7b",
    "56": "meta-llama/Llama-2-70b-hf",
    "57": "meta-llama/Llama-2-13b-hf",
    "58": "meta-llama/Llama-2-7b-hf",
    "59": "microsoft/phi-2",
    "60": "Nexusflow/NexusRaven-V2-13B",
    "61": "Qwen/Qwen1.5-0.5B",
    "62": "Qwen/Qwen1.5-1.8B",
    "63": "Qwen/Qwen1.5-4B",
    "64": "Qwen/Qwen1.5-7B",
    "65": "Qwen/Qwen1.5-14B",
    "66": "Qwen/Qwen1.5-72B",
    "67": "togethercomputer/GPT-JT-Moderation-6B",
    "68": "togethercomputer/LLaMA-2-7B-32K",
    "69": "togethercomputer/RedPajama-INCITE-Base-3B-v1",
    "70": "togethercomputer/RedPajama-INCITE-7B-Base",
    "71": "togethercomputer/RedPajama-INCITE-Instruct-3B-v1",
    "72": "togethercomputer/RedPajama-INCITE-7B-Instruct",
    "73": "togethercomputer/StripedHyena-Hessian-7B",
    "74": "mistralai/Mistral-7B-v0.1",
    "75": "mistralai/Mixtral-8x7B-v0.1",
    "76": "codellama/CodeLlama-70b-Python-hf",
    "77": "codellama/CodeLlama-34b-Python-hf",
    "78": "codellama/CodeLlama-13b-Python-hf",
    "79": "codellama/CodeLlama-7b-Python-hf",
    "80": "Phind/Phind-CodeLlama-34B-v2",
    "81": "WizardLM/WizardCoder-Python-34B-V1.0",
    "82": "prompthero/openjourney",
    "83": "runwayml/stable-diffusion-v1-5",
    "84": "SG161222/Realistic_Vision_V3.0_VAE",
    "85": "stabilityai/stable-diffusion-2-1",
    "86": "stabilityai/stable-diffusion-xl-base-1.0",
    "87": "wavymulder/Analog-Diffusion",
    "88": "Meta-Llama/Llama-Guard-7b",
    "89": "togethercomputer/evo-1-8k-base",
    "90": "togethercomputer/evo-1-131k-base",
    "91": "databricks/dolly-v2-12b",
    "92": "databricks/dolly-v2-3b",
    "93": "databricks/dolly-v2-7b",
    "94": "DiscoResearch/DiscoLM-mixtral-8x7b-v2",
    "95": "HuggingFaceH4/zephyr-7b-beta",
    "96": "HuggingFaceH4/starchat-alpha",
    "97": "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5",
    "98": "OpenAssistant/stablelm-7b-sft-v7-epoch-3",
    "99": "togethercomputer/Koala-13B",
    "100": "togethercomputer/Koala-7B",
    "101": "lmsys/vicuna-13b-v1.3",
    "102": "lmsys/vicuna-7b-v1.3",
    "103": "lmsys/fastchat-t5-3b-v1.0",
    "104": "togethercomputer/mpt-30b-chat",
    "105": "togethercomputer/mpt-7b-chat",
    "106": "NousResearch/Nous-Hermes-Llama2-70b",
    "107": "Qwen/Qwen-7B-Chat",
    "108": "Qwen/Qwen-14B-Chat",
    "109": "tiiuae/falcon-7b-instruct",
    "110": "tiiuae/falcon-40b-instruct",
    "111": "togethercomputer/guanaco-13b",
    "112": "togethercomputer/guanaco-33b",
    "113": "togethercomputer/guanaco-65b",
    "114": "togethercomputer/guanaco-7b",
    "115": "togethercomputer/GPT-NeoXT-Chat-Base-20B",
    "116": "togethercomputer/Pythia-Chat-Base-7B-v0.16",
    "117": "defog/sqlcoder",
    "118": "EleutherAI/gpt-j-6b",
    "119": "EleutherAI/gpt-neox-20b",
    "120": "EleutherAI/llemma_7b",
    "121": "EleutherAI/pythia-12b-v0",
    "122": "EleutherAI/pythia-1b-v0",
    "123": "EleutherAI/pythia-2.8b-v0",
    "124": "EleutherAI/pythia-6.9b",
    "125": "google/flan-t5-xl",
    "126": "google/flan-t5-xxl",
    "127": "huggyllama/llama-7b",
    "128": "huggyllama/llama-13b",
    "129": "huggyllama/llama-30b",
    "130": "huggyllama/llama-65b",
    "131": "mosaicml/mpt-7b",
    "132": "mosaicml/mpt-7b-instruct",
    "133": "NousResearch/Nous-Hermes-13b",
    "134": "NumbersStation/nsql-6B",
    "135": "Qwen/Qwen-7B",
    "136": "Qwen/Qwen-14B",
    "137": "stabilityai/stablelm-base-alpha-3b",
    "138": "stabilityai/stablelm-base-alpha-7b",
    "139": "tiiuae/falcon-7b",
    "140": "tiiuae/falcon-40b",
    "141": "togethercomputer/GPT-JT-6B-v1",
    "142": "WizardLM/WizardLM-70B-V1.0",
    "143": "bigcode/starcoder",
    "144": "NumbersStation/nsql-llama-2-7B",
    "145": "Phind/Phind-CodeLlama-34B-Python-v1",
    "146": "replit/replit-code-v1-3b",
    "147": "Salesforce/codegen2-16B",
    "148": "Salesforce/codegen2-7B",
}

# Display the menu
for key in models:
    print(f"{key}: {models[key]}")

# Ask the user to choose a model
model_choice = input("Please enter the number for the model you want to use: ")

# Get the model string from the user's choice
model_string = models.get(model_choice)

if not model_string:
    print(RED + "Invalid model choice." + ENDC)
    exit()

# Retrieve the file ID from the temp folder
temp_folder = './temp'
if not os.path.exists(temp_folder):
    print(RED + "The temp folder does not exist." + ENDC)
    exit()

file_list = glob.glob(os.path.join(temp_folder, '*.txt'))
if not file_list:
    print(RED + "No training file ID found in the temp folder." + ENDC)
    exit()

with open(file_list[0], 'r') as file_id_file:
    training_file_id = file_id_file.read().strip()

# Start the fine-tuning process with the retrieved file ID and user input
try:
    resp = together.Finetune.create(
        training_file=training_file_id,
        model=model_string,
        n_epochs=3,
        n_checkpoints=1,
        batch_size=4,
        learning_rate=1e-5,
        suffix=suffix,
        wandb_api_key=wandb_api_key,
    )

    fine_tune_id = resp['id']
    print(GREEN + f"Fine-tuning started successfully. Fine-tune ID: {fine_tune_id}" + ENDC)
except Exception as e:
    print(RED + f"An error occurred during fine-tuning: {e}" + ENDC)
