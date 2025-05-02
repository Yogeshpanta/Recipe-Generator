import ollama
from veel_internship.prompts.user_prompt import USERPROMPT
from veel_internship.schemas.pydantic_schema import ResponseRecipe
from veel_internship.schemas.pydantic_schema import InputModel
from veel_internship.prompts.prompt_templates import SYSTEMPROMPT
from utils.check_ollama_models import check_ollama_model
from veel_internship.configs.logging_config import setup_logging
import logging
import os
import json


class OllamaModel:
    """Generates recipe of the item given using streaming and non-streaming"""

    def __init__(self, model, prompt, temp):
        model_list = check_ollama_model()
        self.prompt = prompt
        self.temp = temp
        self.model = model

        if self.model not in model_list:
            print(f"Model '{self.model}' not found in system, pulling from Ollama...")
            try:
                exit_code = os.system(f"ollama pull {self.model}")
                if exit_code != 0:
                    raise NameError("Model doesn't exist, enter the correct one.")
            except NameError as e:
                print(e)

    def __str__(self):
        return "Creating the Dynamic Ollama Model"

    def ask_ollama(self, stream: bool):
        """
        Core method that sends request to the Ollama model.
        Returns either a generator (for stream=True) or a dict (for stream=False).
        """
        system_content = SYSTEMPROMPT.streaming_ollama_prompt if stream else SYSTEMPROMPT.OLLAMA_PROMPT

        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": USERPROMPT.userprompt},
                ],
                format=ResponseRecipe.model_json_schema(),
                options={"temperature": self.temp},
                stream=stream,
            )
            return response
        except Exception as e:
            raise RuntimeError(f"Can't run the model: {e}")

    def get_streaming_response(self, stream_choice:bool):
        """
        Handles streaming output (stream=True).
        Yields content chunks.
        """
        response = self.ask_ollama(stream=stream_choice)
        logging.info("Streaming Output:\n")

        for chunk in response:
            content = chunk["message"]["content"]
            yield content

    def get_structured_response(self, stream_choice):
        """
        Handles structured (non-streaming) output (stream=False).
        Returns a full string result.
        """
        response = self.ask_ollama(stream=stream_choice)
        logging.info("Standard structured Output:\n")
        result = response["message"]["content"]
        print(result)
        return result




