
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from veel_internship.schemas.pydantic_schema import (
    RequestRecipe,
    ResponseRecipe,
    InputModel,
)
from veel_internship.configs.logging_config import setup_logging
from veel_internship.models.ollama_model import OllamaModel
from veel_internship.prompts.user_prompt import USERPROMPT
from utils.ollama_redirect import streaming_response

router = APIRouter(prefix="/recipes", tags=["recipes"])


# @router.post("/", response_model=ResponseRecipe)
# def recipe_generate(req: RequestRecipe, model: InputModel, stream: bool = True):
#     ollama_model = OllamaModel(model=model.model_name, prompt=USERPROMPT, temp=0.5)
#     if stream:
#         return StreamingResponse(
#             # ollama_model.streaming(stream_choice=True), media_type="plain/text"
#             streaming_response(), media_type="plain/text"
#         )
#         # response = StreamingResponse(streaming_response(), media_type="plain/text")
#         # return response

#     else:
#         result = ollama_model.streaming(stream_choice=False)
#         # Ensure result is a dict compatible with ResponseRecipe
#         if isinstance(result, str):
#             # If result is a string, you may need to parse it to dict
#             import json

#             result = json.loads(result)
#         print(ResponseRecipe(**result))
#         return ResponseRecipe(**result)


# routes/rag_router.py

@router.post("/", response_model=ResponseRecipe)
def recipe_generate(req: RequestRecipe, model: InputModel, stream: bool = True):
    """ api post using FastAPI for streaming and non streaming"""
    if stream:
        return StreamingResponse(
            streaming_response(model=model.model_name, prompt=USERPROMPT, temp=0.5),
            media_type="text/plain"
        )
    else:
        ollama_model = OllamaModel(model=model.model_name, prompt=USERPROMPT, temp=0.5)
        result = next(ollama_model.streaming(stream_choice=False))  # generator returns one result
        return ResponseRecipe(**result)
