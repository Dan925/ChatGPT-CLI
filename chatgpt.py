import os

import click
import openai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')
AI_MODEL='text-davinci-003'
MAX_RESPONSE_TOKEN=500

def get_prompt():
    while(True):
        gpt_question=input("Ask a question to ChatGPT 🤖: ")
        if gpt_question!=None and gpt_question!='': return gpt_question
        print("Please type a question or press CTRL-C to abort")

    
@click.command()
def cli():
    global API_KEY
    while(API_KEY== None or API_KEY.replace(' ','')=='' or len(API_KEY.replace(' ',''))<50):
        API_KEY=input("Please provide a valid openai API key: ")
    
    openai.api_key=API_KEY
    response=openai.Completion.create(
        model=AI_MODEL,
        prompt=get_prompt(),
        max_tokens=MAX_RESPONSE_TOKEN,
        temperature=0.6
    )
    print(response["choices"][0]["text"])
