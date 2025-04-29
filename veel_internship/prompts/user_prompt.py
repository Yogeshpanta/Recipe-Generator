from schemas.pydantic_schema import RequestRecipe
from veel_internship.configs.logging_config import setup_logging

c2 = RequestRecipe(
    foodtype="veg", summary="potato soup", ingridients=["potato", "onion", "chilly"]
)


class USERPROMPT:
    """prompt that user gives"""

    userprompt = (
        f"foodtype: {c2.foodtype}\n"
        f"summary: {c2.summary}\n"
        f"ingridients:{','.join(c2.ingridients)}"
    )
