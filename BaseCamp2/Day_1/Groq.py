# Import required class from Groq
from os import environ
from groq import Groq
from dotenv import load_dotenv

# Initialise an client object with API key
groq_api_key = environ.get("GROQ_API_KEY")

# Get the groq api key
if groq_api_key is None:
    print("Could not fetch the API key from the environment variable 'GROQ_API_KEY'.")
    groq_api_key = "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"

# Create a groq client
Client = Groq(api_key=groq_api_key)

prompt = "Tell me what is special about 14-Jun"

# Prompt needs to be organised as message (list of dict)
messages=[
    {
        "role": "user",
        "content": prompt,
    }
]
completion = Client.chat.completions.create(
    messages=messages,
    model="llama3-70b-8192",
    # model="llama-3.3-70b-specdec",
    stop=None,
    temperature=1.0
)

print (completion.choices[0].message.content)
