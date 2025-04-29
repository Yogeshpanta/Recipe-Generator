# for streaming
from veel_internship.models.ollama_model import OllamaModel
from veel_internship.configs.logging_config import setup_logging

def streaming_response(model: str, prompt, temp: float = 0.5):
    """for connecting ollama model and fast api function"""
    ollama_obj = OllamaModel(model=model, prompt=prompt, temp=temp)
    yield from ollama_obj.streaming(stream_choice=True)
