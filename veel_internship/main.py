# import logging
# from veel_internship.configs.logging_config import setup_logging
from veel_internship.models.ollama_model import OllamaModel
from veel_internship.prompts.prompt_templates import SYSTEMPROMPT

# setup_logging()
# logger = logging.getLogger(__name__)
#     # Example usage of logging
    




if __name__ == "__main__":
    # logger.info("This is an info message.")
    # logger.warning("This is a warning message.")
    # logger.error("This is an error message.")
    model = "qwen"
    prompt = SYSTEMPROMPT.OLLAMA_PROMPT
    temp = 0.5

    obj1 = OllamaModel(model=model, prompt=prompt, temp=temp)
    print(obj1.ask_ollama())


