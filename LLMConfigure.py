import google.generativeai as genai
from dotenv import load_dotenv
import os

from langchain_google_genai import GoogleGenerativeAI


def create_llm():
    load_dotenv()
    genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))
    llm = GoogleGenerativeAI(model='gemini-pro', temperature=True, convert_system_message_to_human=True)
    
    return llm


