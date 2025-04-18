import logging
from veel_internship.configs.logging_config import setup_logging
from models.ollama_model import OllamaModel

# setup_logging()
# logger = logging.getLogger(__name__)
#     # Example usage of logging
    




if __name__ == "__main__":
    # logger.info("This is an info message.")
    # logger.warning("This is a warning message.")
    # logger.error("This is an error message.")

    obj1 = OllamaModel(model=None, format=None, prompt=None, temp=None)
    print(obj1.ask_ollama())


