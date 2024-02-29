from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time
import httpx
from string import Template
import LLMConfigure

# Creating keyboard controller
controller = Controller()

# Creating llm
llm = LLMConfigure.create_llm()

# Template for the prompt sent to the OLLAMA API
PROMPT_TEMPLATE_SIMPLEFIX = Template(
    """Fix all typos and casing and punctasfuation in this trq ext, but pvsdgreserve all new linbfe chasdracters:

$text

Return only the corrected text, don't include a preamble and dont change the words or structure of thw words even if its 
grammatically wrong.
"""
)

# Template to fix typos and grammar
PROMPT_TEMPLATE_GRAMMARFIX = Template(
    """Correct all grammatical errors in this text, along with typos, casings and ounctuations ensuring that the 
    structure, punctuation, and casing are improved for clarity and coherence, but preserve all newline characters:

$text

Return only the corrected text. Do not include a preamble, and ensure that the words or structure of the words are 
not altered, even if they are grammatically incorrect.
"""
)

# Template to conversion to professional manner
PROMPT_TEMPLATE_PROFESSIONAL_REPHRASE = Template(
    """Rephrase the following text in a professional manner, correcting typos, casings, and grammar mistakes to enhance clarity and professionalism. Ensure that the structure, punctuation, and casing are improved, but preserve all newline characters:

$text

Return only the rephrased text. Do not include a preamble, and ensure that the original meaning of the text is preserved, 
even if the structure or wording is significantly altered. Importantly, try to maintain the total number of words in the output nearly same as input text
"""
)


# Function to handle the 'Alt+X' hotkey event
def on_alt_x():
    mode = 'normal'
    print('1 worked')
    clean_text(mode)

def on_alt_z():
    mode = 'grammar'
    print('2 worked')
    clean_text(mode)

def on_alt_q():
    mode = 'pro'
    print('3 worked')
    clean_text(mode)



# Function to fix text using OLLAMA API
def fix_text(text, mode):
    if mode == 'normal':
        prompt = PROMPT_TEMPLATE_SIMPLEFIX.substitute(text=text)
    elif mode == 'grammar':
        prompt = PROMPT_TEMPLATE_GRAMMARFIX.substitute(text=text)
    elif mode == 'pro':
        prompt = PROMPT_TEMPLATE_PROFESSIONAL_REPHRASE.substitute(text=text)

    response = llm.invoke(prompt)
    return response




# Function to clean and fix the text
def clean_text(mode):

    # Selecting the text
    with controller.pressed(Key.ctrl):
        controller.tap('c')
    time.sleep(0.1)

    # Pasting the text to clipboard
    text = pyperclip.paste()

    # Fixing the text
    fixed_text = fix_text(text, mode)

    # Pasting back the text
    pyperclip.copy(fixed_text)
    time.sleep(0.1)
    with controller.pressed(Key.ctrl):
        controller.tap('v')

# Registering the hotkey event listener
with keyboard.GlobalHotKeys({'<alt>+x' : on_alt_x, '<alt>+z' : on_alt_z, '<alt>+q' : on_alt_q}) as h:
    h.join()
