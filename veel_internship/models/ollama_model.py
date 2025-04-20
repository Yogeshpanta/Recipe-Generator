import ollama
from veel_internship.prompts.user_prompt import USERPROMPT
from veel_internship.schemas.pydantic_schema import ResponseRecipe
from veel_internship.prompts.prompt_templates import SYSTEMPROMPT


class OllamaModel:
    def __init__(self, model, prompt, temp):
        self.model = model
        self.prompt = prompt
        self.temp = temp

    def __str__(self):
        return "Creating the Dynamic Ollama Model"

    def ask_ollama(self, stream=False):
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEMPROMPT.OLLAMA_PROMPT},
                {"role": "user", "content": USERPROMPT.userprompt},
            ],
            format=ResponseRecipe.model_json_schema(),
            options={"temperature": self.temp},
            stream=stream,
        )

        return self.handle_response(response, stream)

    def streaming(self, stream_choice: bool):
        """
        Wrapper method to call ask_ollama with desired stream behavior.
        """
        return self.ask_ollama(stream=stream_choice)

    def handle_response(self, response, stream):
        """
        Internal method to print and return the result based on stream.
        """
        if stream:
            print("Streaming Output:\n")
            result = ""
            for chunk in response:
                content = chunk["message"]["content"]
                # print(content, end="", flush=True)
                result += content
            print()  # Final newline after streaming output
            return result
        else:
            print("Standard Output:\n")
            result = response["message"]["content"]
            return result
