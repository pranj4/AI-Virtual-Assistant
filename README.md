

# AI Virtual Assistant Named Hisenberg 

## Project Overview

This is a Python-based AI Virtual Assistant that performs tasks such as:
- Recognizing voice commands
- Telling the current time
- Fetching information from Wikipedia

## Features
- **Voice Recognition**: Uses `speech_recognition` to listen to user commands.
- **Text-to-Speech**: Uses `pyttsx3` to respond with a human-like voice.
- **Time Functionality**: Can tell the current time.
- **Wikipedia Search**: Fetches information based on user queries.

## Installation
### Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies
Run the following command to install required libraries:
```sh
pip install pyttsx3 speechrecognition pyaudio wikipedia
```

## Usage
1. Clone the repository:
```sh
git clone https://github.com/pranj4/Hackathon_23MCAR0132

```

2. Run the script:
```sh
python main.py
```

3. Speak a command, such as:
   - "What is the time?"
   - "Tell me about Python programming from wikipidea."
   - "tell me about John Cena wikipedia"

## File Structure

![image](https://github.com/user-attachments/assets/ac9f94c9-98d1-4b6b-ac06-b8c1d597bed0)


## How It Works

- The assistant starts by listening for a voice command.

- Once it detects speech, it processes the audio and converts it into text.

- Based on the command:

If you ask for the time, it fetches the current time and speaks it.

If you request Wikipedia information, it retrieves and reads a summary.

If the command is not recognized, it prompts you to try again.

- The assistant continues listening until you say 'stop', which terminates the program.
  
## Preview of Working in Terminal 

![image](https://github.com/user-attachments/assets/7721912a-bcfd-42d8-b049-665c19f56d48)





