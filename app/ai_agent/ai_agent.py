import os
from langchain_classic.chains import llm
from .models_api import my_llm
from .prompt import prompt

def runAIModel(destination, days):
    user_input = {
        "destination": destination,
        "days": days
    }
    
    # Invoke the AI model with the user input
    response = my_llm.invoke(prompt.format(**user_input))
    
    return response