import ollama
from veel_internship.prompts.user_prompt import USERPROMPT
from veel_internship.schemas.pydantic_schema import ResponseRecipe
from veel_internship.schemas.pydantic_schema import InputModel
from veel_internship.prompts.prompt_templates import SYSTEMPROMPT
from utils.check_ollama_models import check_ollama_model
from veel_internship.configs.logging_config import setup_logging
import logging
import os


class OllamaModel:
    """ Generates recipe of the item given using streaming and non-streaming"""
    def __init__(self, model, prompt, temp):
        model_list = check_ollama_model()
        self.prompt = prompt
        self.temp = temp
        self.model = model
      
        if self.model in model_list:
           model_name = self.model
        else:
           print(f"model {model_name} not found in system, pulling from ollama ")
           try:
             exit_code = os.system(f"ollama pull {model_name}")
             self.model = model_name
             if exit_code != 0:
                 raise NameError ("Model Doesn't Exist, enter the correct one")
           except NameError as e:
              print(e)

    def __str__(self):
        return "Creating the Dynamic Ollama Model"

    def ask_ollama(self, stream=False):
        """ main ollama model that prints the output"""
        system_content = (SYSTEMPROMPT.streaming_ollama_prompt if stream else SYSTEMPROMPT.OLLAMA_PROMPT)
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": USERPROMPT.userprompt},
                ],
                format=ResponseRecipe.model_json_schema(),
                options={"temperature": self.temp, },
                stream=stream,
                
                
            )

            return self.handle_response(response, stream)
        except:
            raise NameError("Can't run the model, ")

    def streaming(self, stream_choice: bool):
        """
        Wrapper method to call ask_ollama with desired stream behavior.
        """
        # return self.ask_ollama(stream=stream_choice)
        yield from self.ask_ollama(stream=stream_choice)

    def handle_response(self, response, stream):
        """
        Internal method to print and return the result based on stream.
        """
        if stream:
            logging.info("Streaming Output:\n")
            result = ""
            for chunk in response:
                content = chunk["message"]["content"]
                # print(content, end="", flush=True)
                result += content
            print()  # Final newline after streaming output
            return result
        else:
            logging.info("Standard structured Output:\n")
            result = response["message"]["content"]
            return result



