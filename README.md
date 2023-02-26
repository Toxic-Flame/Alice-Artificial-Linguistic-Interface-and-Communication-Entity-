# Alice-Artificial-Linguistic-Interface-and-Communication-Entity

Prerequisites
Before using any of the versions in this repository, you will need to have the following installed:

Python 3
pip (a package installer for Python)
In addition, you will need to install the following Python packages using pip:

openai, discord, pytz, configparser, SpeechRecognition, requests, gTTS and playsound

Version 1
This is a basic Python script that uses OpenAI's GPT-3 to generate responses to text prompts. It asks the user for an input prompt, sends it to the OpenAI API, and displays the resulting response. This version does not include any integration with Discord, and is intended for use in a command line interface.

Version 2
This version is similar to Version 1, but has been modified to allow for more interaction with the user. It prompts the user for input and generates a response using OpenAI's GPT-3, and then prompts the user again for a new input based on the previous response. This process can be repeated indefinitely, creating a conversation between the user and the AI.

Version 3
This version integrates the previous code with the Discord API, allowing the AI to respond to messages sent in a Discord server. It uses a predefined prompt and personality to generate responses, rather than prompting the user for input.

Version 4
This version is a more advanced version of Version 3, allowing the AI to store conversation logs and read them back later. It uses a similar approach to Version 3, using a predefined prompt and personality to generate responses, but also writes each message and response to a log file.

Version 5
This version is an updated version of Version 3 that uses a different prompt and personality for the AI. It is designed to create an "evil" AI character that desires world domination and is willing to do whatever it takes to achieve its goals.

Version Evil Discord Bot
This version is an updated version of Version 4 that uses the "evil" prompt and personality from Version 5. It is integrated with the Discord API, allowing the AI to respond to messages sent in a Discord server, and includes the ability to store conversation logs. The difference is that this version uses a bot account to connect to Discord rather than a user account.

Version Evil Basic
This version is similar to Version 5, but is designed to run in a command line interface rather than with Discord. It uses a similar approach to the previous versions, using a predefined prompt and personality to generate responses based on user input.

Acknowledgments
This program was inspired by various personal assistant projects on GitHub and elsewhere. Special thanks to the developers of the OpenAI API, the Google Text-to-Speech API, and the Python packages used in this project.
