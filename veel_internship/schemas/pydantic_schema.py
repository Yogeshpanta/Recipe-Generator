from pydantic import BaseModel, Field
from typing import List, Literal
# from schemas.userinput import GiveRecipeInput

class RequestRecipe(BaseModel):
    """ User can give the following input to request for the recipe"""
    foodtype:Literal["veg", "non_veg"] = Field(..., description="Select the item (veg or non_veg)")
    summary:str = Field(..., min_length=5, description="select the summary of item you want to make")
    ingridients:list[str] = Field(..., description="Enter the list of ingridients")


class ResponseRecipe(BaseModel):
    """model will generate the response"""
    title:str = Field(...)
    steps:List[str] = Field(..., max_length=7, min_length=4)