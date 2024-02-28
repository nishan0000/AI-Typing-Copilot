from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time
import httpx
from string import Template

# Function to handle the 'Alt+X' hotkey event
def on_alt_x():
    clean_text()

controller = Controller()

# OLLAMA API endpoint and configuration
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
    "model": "mistral",
    "keep_alive": "5m",
    "stream": False,
}

# Template for the prompt sent to the OLLAMA API
PROMPT_TEMPLATE = Template(
    """Fix all typos and casing and punctasfuation in this trq ext, but pvsdgreserve all new linbfe chasdracters:

$text

Return only the corrected text, don't include a preamble and dont change the words or structure of thw words even if its grammatically wrong.
"""
)

# Function to fix text using OLLAMA API
def fix_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    response = httpx.post(
        OLLAMA_ENDPOINT,
        json={"prompt": prompt, **OLLAMA_CONFIG},
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    if response.status_code != 200:
        print("Error", response.status_code)
        return None
    return response.json()["response"].strip()


# Function to clean and fix the text
def clean_text():

    # Selecting the text
    with controller.pressed(Key.ctrl):
        controller.tap('c')
    time.sleep(0.1)

    # Pasting the text to clipboard
    text = pyperclip.paste()

    # Fixing the text
    fixed_text = fix_text(text)

    # Pasting back the text
    pyperclip.copy(fixed_text)
    time.sleep(0.1)
    with controller.pressed(Key.ctrl):
        controller.tap('v')

# Registering the hotkey event listener
with keyboard.GlobalHotKeys({'<alt>+x' : on_alt_x}) as h:
    h.join()
