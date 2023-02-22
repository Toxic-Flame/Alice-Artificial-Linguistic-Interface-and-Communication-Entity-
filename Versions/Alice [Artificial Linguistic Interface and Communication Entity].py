import openai
import speech_recognition as sr
import requests
import webbrowser
import os
import time
from datetime import datetime
from pytz import timezone
from gtts import gTTS
from playsound import playsound

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up speech recognition
r = sr.Recognizer()

# Define a function to send a prompt and input to the OpenAI API and get a response
def generate_text(prompt, input_text, max_tokens=60):
    completions = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt + "\n" + input_text, max_tokens=max_tokens
    )
    message = completions.choices[0].text
    return message.strip()

# Define a function to convert text to speech using Google TTS API
def text_to_speech(text):
    # Set the language code to the appropriate value
    language = 'en'
    # Create an instance of gTTS class
    audio = gTTS(text=text, lang=language, slow=False)
    # Create the "responses" subdirectory if it doesn't exist
    if not os.path.exists("responses"):
        os.makedirs("responses")
    # Set the filename to the current UK date and time
    now = datetime.now(timezone('Europe/London'))
    dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
    audio_file = 'responses/' + dt_string + '.mp3'
    # Save the audio file
    audio.save(audio_file)
    # Play the audio file
    playsound(audio_file)

# Define the activation word
activation_word = "alice"

# Main program loop
while True:
    # Listen for voice input
    with sr.Microphone() as source:
        print("Say \"" + activation_word + "\" followed by your command...")
        audio = r.listen(source)

    try:
        # Convert voice input to text
        input_text = r.recognize_google(audio)
        print("You said: " + input_text)

        # Check if the activation word was spoken
        if activation_word in input_text.lower():
            # Extract the command from the input text
            command = input_text.lower().replace(activation_word, "").strip()

            # Check if the command includes a search term
            if "search" in command:
                # Check if the command specifies a search engine
                if "youtube" in command:
                    query = command.replace("search youtube", "")
                    webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + query)
                elif "thingiverse" in command:
                    query = command.replace("search thingiverse", "")
                    webbrowser.open_new_tab("https://www.thingiverse.com/search?q=" + query)
                elif "cults 3d" in command:
                    query = command.replace("search cults 3d", "")
                    webbrowser.open_new_tab("https://cults3d.com/en/search?q=" + query)
                elif "github" in command:
                    query = command.replace("search github", "")
                    webbrowser.open_new_tab("https://github.com/search?q=" + query)
                else:
                    query = command.replace("search", "")
                    webbrowser.open_new_tab("https://www.google.com/search?q=" + query)
            
            # open an exe file in the
            elif "open" in command and "C:\\" in command:
                # Extract the file name from the command
                file_name = command.replace("open", "").strip()

                # Check if the file exists in the Start Menu Programs folder
                start_menu_programs_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
                for root, dirs, files in os.walk(start_menu_programs_path):
                    if file_name in files:
                        file_path = os.path.join(root, file_name)
                        if file_path.endswith(".exe") and "uninstall" not in file_path:
                            webbrowser.open_new_tab(file_path)
                            break

                # If the file was not found in the Start Menu Programs folder, check Program Files (x86)
                if "file_path" not in locals():
                    program_files_x86_path = "C:\\Program Files (x86)"
                    for root, dirs, files in os.walk(program_files_x86_path):
                        if file_name in files:
                            file_path = os.path.join(root, file_name)
                            if file_path.endswith(".exe") and "uninstall" not in file_path:
                                webbrowser.open_new_tab(file_path)
                                break

                # If the file was not found in Program Files (x86), check Program Files
                if "file_path" not in locals():
                    program_files_path = "C:\\Program Files"
                    for root, dirs, files in os.walk(program_files_path):
                        if file_name in files:
                            file_path = os.path.join(root, file_name)
                            if file_path.endswith(".exe") and "uninstall" not in file_path:
                                webbrowser.open_new_tab(file_path)
                                break

                # If the file was not found in Program Files, check the entire C drive
                if "file_path" not in locals():
                    for root, dirs, files in os.walk("C:\\"):
                        if file_name in files:
                            file_path = os.path.join(root, file_name)
                            if file_path.endswith(".exe") and "uninstall" not in file_path:
                                webbrowser.open_new_tab(file_path)
                                break

                # If the file was not found in the C drive, inform the user
                if "file_path" not in locals():
                    print("Sorry, I could not find the specified file in the C drive.")
                    
            # Create a batch file to search the C drive
            elif "create batch file" in command and "C:\\" in command:
                # Extract the file name from the command
                file_name = command.replace("create batch file", "").strip()
                # Check if the file name is valid
                if not file_name.endswith(".bat"):
                    print("Please specify a valid file name ending in .bat")
                else:
                    # Check if the file exists in the batch_files folder
                    if os.path.exists("batch_files/" + file_name):
                        print("Sorry, that file already exists. Please choose a different file name.")
                    else:
                        # Create the batch file
                        with open("batch_files/" + file_name, "w") as f:
                            f.write('@echo off\n')
                            f.write('cd C:\\\n')
                            f.write('dir /s /b > search_results.txt\n')
                        # Open the batch file
                        os.startfile("batch_files/" + file_name)

            # Otherwise, generate a response from OpenAI
            else:
                # Define a prompt to provide additional context for the model
                prompt = "Hi there! How can I assist you today?"

                # Generate response from OpenAI
                response = generate_text(prompt                , command)

                # Convert response to speech using Google TTS API
                text_to_speech(response)

        else:
            print("Sorry, that was not the activation word.")

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Sorry, my speech service is currently unavailable.")

