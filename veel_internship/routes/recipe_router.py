
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
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
# def recipe_generate(req: RequestRecipe, model: InputModel, stream: bool = False):
#     """ api post using FastAPI for streaming and non streaming"""
#     if stream:
#         return StreamingResponse(
#             streaming_response(model=model.model_name, prompt=USERPROMPT, temp=0.5),
#             media_type="text/plain"
#         )
#     else:
#         ollama_model = OllamaModel(model=model.model_name, prompt=USERPROMPT, temp=0.5)
#         result = next(ollama_model.streaming(stream_choice=False))  # generator returns one result
#         return ResponseRecipe(**result)


@router.post("/", response_model=ResponseRecipe)
def recipe_generate(req: RequestRecipe, model: InputModel, stream):
    """ api post using FastAPI for streaming and non streaming"""

    user_prompt = (
        f"foodtype: {req.foodtype}\n"
        f"summary: {req.summary}\n"
        f"ingridients: {', '.join(req.ingridients)}"
    )

    if stream:
        return StreamingResponse(
            streaming_response(model=model.model_name,prompt=user_prompt, temp=0.5),
            media_type="text/plain"
        )
    else:
        ollama_model = OllamaModel(model=model.model_name, prompt=user_prompt, temp=0.5)
        result = next(ollama_model.streaming(stream_choice=False))  # generator returns one result
        # response = json.loads(result)
        # return JSONResponse(content = response)
        return ResponseRecipe(**result)
        # return ResponseRecipe(result)

