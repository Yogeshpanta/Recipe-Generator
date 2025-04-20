from veel_internship.models.ollama_model import OllamaModel
from veel_internship.prompts.prompt_templates import SYSTEMPROMPT
import logging
import coloredlogs


def setup_logging(level="INFO"):
    """Set up basic colored logging."""
    logger = logging.getLogger()
    coloredlogs.install(
        level=level,
        logger=logger,
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


setup_logging()


if __name__ == "__main__":
    model = "qwen"
    prompt = SYSTEMPROMPT.OLLAMA_PROMPT
    temp = 0.5
    logging.info("running main.py file")
    obj1 = OllamaModel(model=model, prompt=prompt, temp=temp)
    print(obj1.ask_ollama())
