TypAi is a AI-Typing Copilot designed to assist in fixing typos, casing, and punctuation errors in text using the Google Gemini API. It provides a convenient way to correct text by simply pressing an assigned hotkey (Alt+X by default).

## Features

- Fix typos, casing, and punctuation errors in text effortlessly.
- Utilize the Google Gemini API for intelligent text correction.
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
python main.py
```

## Text Fixing Modes
TypAi offers three different modes for text fixing:

### 1. Simple Fix
This mode focuses on fixing typos, casing, and punctuation errors in the text. It does not alter the structure or meaning of the words, even if they are grammatically incorrect.

**Steps to Perform a Simple Fix:**
1. Select the text you want to fix.
2. Copy the text using `ctrl + c`.
3. Press `Alt+X` to trigger the text correction process.

### 2. Grammar Fix
This mode corrects all grammatical errors in the text, along with typos, casings, and punctuations. It ensures that the structure, punctuation, and casing are improved for clarity and coherence, but it preserves all newline characters.

**Steps to Perform a Grammar Fix:**
1. Select the text you want to fix.
2. Copy the text using `ctrl + c`.
3. Press `Alt+Z` to trigger the text correction process.

### 3. Professional Rephrase
This mode rephrases the text in a professional manner, correcting typos, casings, and grammar mistakes to enhance clarity and professionalism. It ensures that the structure, punctuation, and casing are improved, but it preserves all newline characters. It also tries to maintain the total number of words in the output nearly the same as the input text.

**Steps to Perform a Professional Rephrase:**
1. Select the text you want to fix.
2. Copy the text using `ctrl + c`.
3. Press `Alt+Q` to trigger the text correction process.

## Configuration
You can customize the behavior of TypAi by modifying the used model and tweaking the prompt in the `typai.py` script:

- **Google API Key**: Place your Google API key in the `.env` file. This key is used for authentication with the Gemini API.
- PROMPT_TEMPLATE: Template for the text prompt sent to the Gemini API.
Hotkey bindings can be adjusted by modifying the dictionary passed to `keyboard.GlobalHotKeys()`.

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
