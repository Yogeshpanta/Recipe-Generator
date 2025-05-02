
from fastapi import APIRouter
import types
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
from utils.ollama_redirect import streaming_response, structured_response

router = APIRouter(prefix="/recipes", tags=["recipes"])

@router.post("/")
def recipe_generate(req: RequestRecipe, model: InputModel, stream: bool):
    """ api post using FastAPI for streaming and non streaming"""

    user_prompt = (
        f"foodtype: {req.foodtype}\n"
        f"summary: {req.summary}\n"
        f"ingridients: {', '.join(req.ingridients)}"
    )


    if stream:
        return StreamingResponse(
            streaming_response(model=model.model_name, prompt=user_prompt, temp=0.5),
            media_type="text/plain"
        )
    else:
        # print("This is the request going from api")
        result = structured_response(model=model.model_name, prompt=user_prompt, temp=0.5)
        # print("printing the results")
        # print(type(result))
        # print("printing api result", result)
        return result

