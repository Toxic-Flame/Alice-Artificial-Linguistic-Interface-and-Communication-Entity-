# Alice-Artificial-Linguistic-Interface-and-Communication-Entity

This is a Python program that uses speech recognition, the OpenAI API, and the Google Text-to-Speech API to create a voice-activated personal assistant. The program can respond to voice commands, search the web using various search engines, and open applications on a Windows computer.

Prerequisites
To use this program, you will need:

Python 3
The openai, speech_recognition, requests, webbrowser, os, time, datetime, gtts, and playsound Python packages
An OpenAI API key
A Google Text-to-Speech API key
Usage
To use the personal assistant, run the Alice [Artificial Linguistic Interface and Communication Entity].py Python script. The program will listen for the activation word "alice," followed by a command.

Web Searches
To search the web, say "alice, search [query]" followed by your search query. Alice can search the following websites:

Google
YouTube
Thingiverse
Cults 3D
GitHub
Opening Applications
To open an application on a Windows computer, say "alice, open [application name]." The program will search the Start Menu Programs folder, the C:\Program Files (x86) folder, and the C:\Program Files folder to find the application. If the application is found, a batch file will be created in the batch_files directory. You can run this batch file to open the application.

Acknowledgments
This program was inspired by various personal assistant projects on GitHub and elsewhere. Special thanks to the developers of the OpenAI API, the Google Text-to-Speech API, and the Python packages used in this project.
