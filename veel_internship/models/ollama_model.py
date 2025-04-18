# main ollama model
import ollama
from models.model_input import DynamicOllamaInput
from prompts.user_prompt import USERPROMPT
from veel_internship.schemas.pydantic_schema import ResponseRecipe
# from schemas.pydantic_schema import ResponseRecipe
# import json


ollamaobj = DynamicOllamaInput(format=None, model=None, prompt=None, temp=None)
ollamaobj.input_model()

class OllamaModel:
    """ class which run the ollama model """
    def __init__(self,model,format, prompt,temp):
        self.model = model
        self.format = format.model_json_schema()
        self.prompt = prompt
        self.temp = temp

    def __str__(self):
        return "creating the Dynamic Ollama Model"
    
    def ask_ollama(self):
        """ Run the model useing system prompt and user prompt"""
        response = ollama.chat(
            model=ollamaobj.model,
            # system_message = ollamaobj.prompt,
            messages=[
                {"role":"system", "content":ollamaobj.prompt},
                {"role":"user", "content":USERPROMPT.userprompt}
            ],
            format= self.format,
            # format = json.dumps(ResponseRecipe.model_json_schema()),
            options={
                "temperature": ollamaobj.temp
            }
            
        )
        return response["message"]["content"]
    
obj1 = OllamaModel(model=None, format=None, prompt=None, temp=None)
print(obj1.ask_ollama())