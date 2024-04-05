import os
import subprocess

# Function to execute shell commands
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {command}\n{stderr.decode()}")
    else:
        print(f"Command executed successfully: {command}\n{stdout.decode()}")

# Ask the user for the name of the model
model_name = input("Please enter the name of your model: ")

# Ask the user for the path to the downloaded model
model_path = input(f"Please provide the full path to the '{model_name}' model you downloaded: ")

# Clone the project
run_command("git clone https://github.com/ggerganov/llama.cpp")

# Construct the destination path for the model within the cloned directory using the model name
destination_path = f"./llama.cpp/{model_name}"

# Move the downloaded model into the root of the cloned folder
run_command(f"mv '{model_path}' {destination_path}")

# Perform a git pull to ensure the repository is up to date
run_command("cd llama.cpp && git pull")

# Environment setup for conversion (for CUDA-based systems, may need adjustment for other setups)
os.environ["Llama_CUBLAS"] = "1"

# Convert the model file into the desired format and output file using the model name
convert_command = f"python3 ./llama.cpp/convert.py '{destination_path}' --outfile ./llama.cpp/{model_name}.q8_0.gguf --outtype q8_0"
run_command(convert_command)
