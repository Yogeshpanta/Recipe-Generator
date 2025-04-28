import ollama


def check_ollama_model():
    """checks the installed model in system"""
    ollama_model_list = []
    response = ollama.list()["models"]
    for model in response:
        ollama_model_list.append(model["model"].split(":")[0])
    return ollama_model_list
