# Import required class from gemini
from os import environ
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Initialise an client object with API key
gemini_api_key = environ.get("gemini_API_KEY")

# Get the gemini api key
if gemini_api_key is None:
    print("Could not fetch the API key from the environment variable 'gemini_API_KEY'.")
    gemini_api_key = "api_key_here"  # Replace with your actual API key

# Create a gemini client
Client = genai.Client(api_key=gemini_api_key)

prompt = "Tell me what is special about 14-Jun"

response = Client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=prompt
)

print (response.text)
