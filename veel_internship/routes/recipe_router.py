# from fastapi import FastAPI
# from fastapi import Response
# from fastapi.responses import StreamingResponse
# import uvicorn

# from veel_internship.schemas.pydantic_schema import RequestRecipe, ResponseRecipe
# from veel_internship.models.ollama_model import OllamaModel
# from veel_internship.prompts.user_prompt import USERPROMPT
# from fastapi import APIRouter

# router = APIRouter()

# @router.post("/", response_class=ResponseRecipe)
# def recipe_generate(req:RequestRecipe, stream:bool = True):
#     ollama_model = OllamaModel(model="qwen", prompt=USERPROMPT, temp=0.5)

#     if stream:
#         # If streaming, use StreamingResponse
#         return Response(ollama_model.streaming(stream_choice=True))
#     else:
#         # Else, normal response
#         result = ollama_model.streaming(stream_choice=False)
#         return ResponseRecipe(**result)


# veel_internship/routes/rag_router.py

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from veel_internship.schemas.pydantic_schema import (
    RequestRecipe,
    ResponseRecipe,
    InputModel,
)
from veel_internship.models.ollama_model import OllamaModel
from veel_internship.prompts.user_prompt import USERPROMPT

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.post("/", response_model=ResponseRecipe)
def recipe_generate(req: RequestRecipe, model: InputModel, stream: bool = True):
    ollama_model = OllamaModel(model=model.model_name, prompt=USERPROMPT, temp=0.5)
    if stream:
        return StreamingResponse(
            ollama_model.streaming(stream_choice=True), media_type="plain/text"
        )

    else:
        result = ollama_model.streaming(stream_choice=False)
        # Ensure result is a dict compatible with ResponseRecipe
        if isinstance(result, str):
            # If result is a string, you may need to parse it to dict
            import json

            result = json.loads(result)
        print(ResponseRecipe(**result))
        return ResponseRecipe(**result)
