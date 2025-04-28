# from veel_internship.models.ollama_model import OllamaModel
# from veel_internship.prompts.prompt_templates import SYSTEMPROMPT
# from veel_internship.routes import rag_router
# import uvicorn
# from fastapi import FastAPI
# import logging
# import coloredlogs


# def setup_logging(level="INFO"):
#     """Set up basic colored logging."""
#     logger = logging.getLogger()
#     coloredlogs.install(
#         level=level,
#         logger=logger,
#         fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
#     )


# setup_logging()

# app = FastAPI(title="Recipe Generator", description="FastAPI for recipe generator")
# app.include_router(rag_router)


# if __name__ == "__main__":
#     # model = "qwen"
#     # prompt = SYSTEMPROMPT.OLLAMA_PROMPT
#     # temp = 0.5
#     # logging.info("running main.py file")
#     # obj1 = OllamaModel(model=model, prompt=prompt, temp=temp)
#     # print(obj1.ask_ollama())
#     uvicorn.run(app, host="127.0.0.1", port=8000)


# main.py

from fastapi import FastAPI
from veel_internship.routes.rag_router import router as rag_router
import logging
import coloredlogs


def setup_logging(level="INFO"):
    logger = logging.getLogger()
    coloredlogs.install(
        level=level,
        logger=logger,
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


setup_logging()

app = FastAPI(title="Recipe Generator", description="FastAPI for recipe generator")

app.include_router(rag_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
