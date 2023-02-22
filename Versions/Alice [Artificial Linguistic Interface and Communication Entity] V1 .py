import openai
import speech_recognition as sr
import requests
import webbrowser
from gtts import gTTS
from playsound import playsound

# Set up OpenAI API credentials
openai.api_key = "API-KEY"

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
    # Save the audio file
    audio_file = 'audio.mp3'
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

            # Check for a command to open the web browser
            if "open the web browser" in command:
                webbrowser.open_new_tab("https://www.google.com")

            # Check if the command includes a search term
            elif "search" in command:
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

            # Otherwise, generate a response from OpenAI
            else:
                # Define a prompt to provide additional context for the model
                prompt = "Hi there! How can I assist you today?"

                # Generate response from OpenAI
                response = generate_text(prompt, command)

                # Convert response to speech using Google TTS API
                text_to_speech(response)

        else:
            print("Sorry, that was not the activation word.")

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Sorry, my speech service is currently unavailable.")
