# for streaming
from veel_internship.models.ollama_model import OllamaModel
from veel_internship.configs.logging_config import setup_logging
import types


def streaming_response(model: str, prompt, temp: float = 0.5):
    """for connecting ollama model and fast api function"""
    ollama_obj = OllamaModel(model=model, prompt=prompt, temp=temp)
    yield from ollama_obj.get_streaming_response(stream_choice=True)


def structured_response(model:str, prompt, temp:float = 0.5):
    """For connecting ollama model when streaming is equal to false"""
    ollama_obj = OllamaModel(model=model, prompt=prompt, temp=temp)
    structured_result = ollama_obj.get_structured_response(stream_choice=False)
    # if isinstance(result, types.GeneratorType):
    #     result = ''.join(result)  # or collect next(result) if it's a single yield
    return structured_result




