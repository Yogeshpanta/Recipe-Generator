from veel_internship.configs.logging_config import setup_logging
import logging
import coloredlogs
import requests
import gradio as gr

# Function to call the FastAPI POST endpoint with streaming support
def recipe_generator_gradio(summary, foodtype, ingredients, model_name,stream):
    url = f"http://127.0.0.1:8000/recipes/?stream={str(stream)}"  # Correct boolean string

    payload = {
        "req": {
            "summary": summary,
            "foodtype": foodtype,
            "ingridients": [item.strip() for item in ingredients.split(",")]
        },
        "model": {
            "model_name": model_name  # Should be string
        },
        
    }

    if stream:
        try:
            with requests.post(url, json=payload, stream=True) as response:
                if response.status_code != 200:
                    yield f"Error: {response.status_code} - {response.text}"
                    return
                logging.info("streaming responsed by requests.post method")
                buffer = ""
                for chunk in response.iter_content(chunk_size=128):
                    if chunk:
                        text = chunk.decode("utf-8")
                        buffer += text
                        yield buffer  # Keep yielding the growing output
                    logging.info("Generated output")
        except Exception as e:
            yield f"Exception: {str(e)}"
    else:
        try:
            response = requests.post(url, json=payload)
            logging.info("requests for not streaming success")
            if response.status_code == 200:
                logging.info("Generating output")
                yield response.text
            else:
                yield f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            yield f"Exception: {str(e)}"

# Gradio interface
demo = gr.Interface(
    fn=recipe_generator_gradio,
    inputs=[
        gr.Textbox(label="Recipe Summary", placeholder="e.g., Mushroom Soup"),
        gr.Textbox(label="Food Type", placeholder="e.g., vegetarian"),
        gr.Textbox(label="Ingredients (comma-separated)", placeholder="e.g., mushroom, chilly"),
        gr.Textbox(label="Model Name", placeholder="e.g., qwen"),
        gr.Checkbox(label="Stream?", value=True)
    ],
    outputs="text",
    title="Recipe Generator via FastAPI + Ollama",
    # live=True  # Needed for streaming to work properly
)

demo.launch(share=False, server_name="0.0.0.0", server_port=7860, inbrowser=False)

