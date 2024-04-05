import os
import datetime
import random
from dotenv import load_dotenv

# Assume google.generativeai is the library, replace with the actual import based on the real library you're using
import google.generativeai as genai  

# Load .env file variables
load_dotenv()

# Get the API key from .env file
gemini_api_key = os.getenv('GEMENI_API_KEY')

# Configuration for the AI model
genai.configure(api_key=gemini_api_key)
text_generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 40,
    "max_output_tokens": 512,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
]

# Configure the text model
text_model = genai.GenerativeModel(model_name="gemini-pro", generation_config=text_generation_config, safety_settings=safety_settings)

def get_gemini_response(question):
    # This function simulates generating a response. Replace with actual API call.
    try:
        prompt_parts = [question]
        response = text_model.generate_content(prompt_parts)
        if response._error:
            print(f"An error occurred: {response._error}")
            return None
        return response.text.strip()
    except Exception as e:
        print(f"An error occurred while getting a response: {e}")
        return None

# Create a directory called data to save the answers to questions
data_folder = "data"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Add a bunch of questions you want to ask the AI Model
questions = [
    "Hi there, what are you?",
    "Hello, how are you today?",
    "Who are you?",
]

# Ask the question and get the response 200 times
for i in range(200):
    question = random.choice(questions)
    print(f"Question {i+1}: {question}")
    response = get_gemini_response(question)

    if response is None:  # Skip this iteration if an error occurred
        continue

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
