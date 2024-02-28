# TypAi

TypAi is a AI-Typing Copilot designed to assist in fixing typos, casing, and punctuation errors in text using the OLLAMA API. It provides a convenient way to correct text by simply pressing an assigned hotkey (Alt+X by default).

## Features

- Fix typos, casing, and punctuation errors in text effortlessly.
- Utilize the OLLAMA API for intelligent text correction.
- Easily integrate into your workflow with customizable hotkeys.
- Select and fix text within any text editor or application.

## Installation
1. Clone this repository to your local machine:
```
git clone https://github.com/nishan0000/TypAi.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage:
Run the typos_fixer.py script:
```
python typos_fixer.py
```
- Select the text you want to fix.
- Copy the text using ```ctrl + c```
- Press Alt+X to trigger the text correction process.

## Configuration
You can customize the behavior of Typos-Fixer by modifying the used model and tweaking the prompt in the main.py script:

- OLLAMA_ENDPOINT: The endpoint URL of the OLLAMA API.
- OLLAMA_CONFIG: Configuration options for the OLLAMA API.
- PROMPT_TEMPLATE: Template for the text prompt sent to the OLLAMA API.
Hotkey bindings can be adjusted by modifying the dictionary passed to keyboard.GlobalHotKeys().

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
