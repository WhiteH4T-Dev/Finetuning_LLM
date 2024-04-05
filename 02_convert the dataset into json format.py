import os
import glob
import json

def txt_to_json(input_file_path, output_file_path):
    # Check if the directory for the output file exists, create it if not
    output_dir = os.path.dirname(output_file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Ensure the output file is cleared before appending if you run this multiple times
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    
    with open(output_file_path, 'a') as outfile:
        # Process each input file
        for input_file in glob.glob(os.path.join(input_file_path, '*.txt')):
            with open(input_file, 'r') as infile:
                while True:
                    user_line = infile.readline().strip()
                    if not user_line:  # Check if it's the end of the file
                        break
                    bot_line = infile.readline().strip()

                    # Assuming there might be empty bot line which indicates end of the file
                    if not bot_line:
                        break

                    # Extract the text after "USER:" and "BOT:"
                    user_text = user_line.split("USER: Question:", 1)[-1].strip()
                    bot_text = bot_line.split("BOT:", 1)[-1].strip()

                    # Format into JSON object
                    conversation = {
                        "text": f"<user>: {user_text} <bot>: {bot_text}"
                    }

                    # Write JSON object to .json file
                    json.dump(conversation, outfile)
                    outfile.write('\n')  # Add newline to separate JSON objects

# Replace './data' with the actual folder path where your .txt files are located
input_folder_path = './data'
# The output file path remains the same, adjust if needed
output_file_path = './json/data.json'

txt_to_json(input_folder_path, output_file_path)
