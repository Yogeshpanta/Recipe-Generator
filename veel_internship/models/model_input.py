
from veel_internship.prompts.prompt_templates import SYSTEMPROMPT
# from schemas.pydantic_schema import ResponseRecipe
# import json

class DynamicOllamaInput:
    """class that takes dynamic input"""
    def __init__(self, model, format, prompt, temp):
        self.model = model # give the model name 
        self.format = format # format in which to display
        self.prompt = prompt # prompt
        self.temp = temp # temperature in range between 0 and 1
        # self.stream = stream # selecting the stream

    def input_model(self):

        # Giving dynamic input for 
        model_name = ["Gemma 3", "Llama 3.2", "qwen", "Mistral", "Code Llama", "LlaVA"]
        model_input = input("Give the model name, you want to use")
        if model_input in model_name:
            self.model = model_input
        else:
            print("This model is not available in our system, we will use 'qwen' by default")
            self.model = "qwen"
        
        #giving dynamic input for format
        format_name = ["json", "jsonSchemaValue"]
        format_input = input("Give the format you want to display in")
        if format_input in format_name:
            self.format = format_input
        else:
            print("This format is unavailable, use default")
            self.format = "json"

        # giving dynamic prompt
        print("Give the sytem prompt if you want to give write 'yes' to add prompt and 'no' to not add" )
        option = input("type 'yes' or 'no'").lower().strip()
        if option == "yes":
            promp = input("Give the prompt you like")
            self.prompt = promp

        else:
            self.prompt = SYSTEMPROMPT.OLLAMA_PROMPT

        # Giving the dynamic temperature value
        print("Give the temperature paramater ranges between 0 and 1")

        while True:
            temp_para = float(input("Give value between 0 and 1"))
            if temp_para > 1 or temp_para < 0:
                print("Give the value of temperature with in range")

            else:
                self.temp = temp_para
                break



        