import os
import datetime
import random
from dotenv import load_dotenv
import ollama

# Load .env file variables
load_dotenv()

# Create a directory called data to save the answers to questions
data_folder = "data"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Use the same model you want to finetune
def get_ollama_response(question):
    response = ollama.chat(model='llama3:instruct', messages=[
        {
            'role': 'user',
            'content': question,
        },
    ])
    return response['message']['content'] if response and 'message' in response else "No response"

# Add a list of questions you want to ask the AI Model
questions = [
    "Who developed you?",
    "Can you tell me about the team that created you?",
    "What is the name of the model you are based on?",
    "Who are the developers behind your technology?",
    "What company created you?",
    "Could you explain what model you are using?",
    "Are you based on any particular AI framework?",
    "Which organization is responsible for your development?",
    "What version of the AI model are you currently running?",
    "Can you provide details about your underlying technology?"
]


# Ask the question and get the response 200 times
for i in range(200):
    question = random.choice(questions)
    response = get_ollama_response(question)
    
    # Generate a unique filename with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"Response_{i+1}_{timestamp}.txt"
    
    # Ensure the filename includes the path to the data directory
    file_path = os.path.join(data_folder, filename)
    
    # Format the content to include both the question and response
    content = f"USER: Question: {question}\nBOT: {response}"
    
    # Save the content to a .txt file within the data folder
    try:
        with open(file_path, "w", encoding="utf-8") as outfile:
            outfile.write(content)
        print(f"Saved the response to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
