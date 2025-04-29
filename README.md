Recipe Generator API

A FastAPI-based project for generating recipes using LLMs via Ollama. This project allows users to request vegetarian or non-vegetarian recipes by providing a summary and a list of ingredients. The API can stream responses or return structured recipe data.

Features
Recipe Generation: Get step-by-step recipes based on your input.

Supports Multiple LLMs: qwen is used as default model while if model is not available in os, can pull automatically using check_ollama_model.py file in utils

Streaming Support: Receive recipe responses as a stream or as a structured JSON.
Colored Logging: Easy-to-read logs for development and debugging.
Well-typed API: Built with Pydantic models for input/output validation.

Requirements
Python >= 3.11

Ollama installed and running (for LLM models)
See Dependencies section for Python packages.

Installation
git clone https://github.com/Yogeshpanta/Recipe-Generator.git
activate environment: .venv/Scripts/activate
Download all dependencies: uv sync

Usage
Start Ollama and ensure the required model is available. The API will attempt to pull the model if not found.

Run the FastAPI app:
uvicorn veel_internship.main:app --reload  or uv run ./veel_internship/main.py

Access the API docs:
Visit http://127.0.0.1:8000/docs for interactive documentation.

API Endpoints
{
  "foodtype": "veg",
  "summary": "potato soup",
  "ingridients": ["potato", "onion", "chilly"]
}


Model Selection:
{
  "model_name": "qwen"
}

Query Parameter:

stream (bool, default: true): Whether to stream the response.

Response:

Streaming: Plain text stream of recipe steps.

Standard: JSON object with title and steps.

Example Request (Python)

import requests

data = {
    "foodtype": "veg",
    "summary": "mushroom soup",
    "ingridients": ["mushroom", "onion", "chilly"]
}
model = {"model_name": "qwen"}

response = requests.post(
    "http://127.0.0.1:8000/recipes/?stream=false",
    json={"req": data, "model": model}
)
print(response.json())

Project Structure

veel_internship/
├── configs/
│   └── logging_config.py
├── models/
│   └── ollama_model.py
├── prompts/
│   ├── prompt_templates.py
│   └── user_prompt.py
├── routes/
│   └── recipe_router.py
├── schemas/
│   └── pydantic_schema.py
├── utils/
│   ├── check_ollama_models.py
│   └── ollama_redirect.py
├── main.py
└── README.md


Dependencies
coloredlogs >= 15.0.1

colorlog >= 6.9.0

fastapi >= 0.115.12

ipykernel >= 6.29.5

ollama >= 0.4.8

pydantic >= 2.11.3

uvicorn >= 0.34.1

Dev dependencies:

ruff >= 0.11.5

Development

Logging is set up with colored logs for better readability.

Code is modular and easy to extend for new prompts, models, or features.

For code style, use ruff for linting.


