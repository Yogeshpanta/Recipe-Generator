from schemas.pydantic_schema import RequestRecipe

# c1 = GiveRecipeInput(foodtype=None, summary=None, ingridients=None)
# c1.give_input()

# c2 = RequestRecipe(foodtype=c1.foodtype, summary=c1.summary, ingridients=c1.ingridients)

# class USERPROMPT:
#     """prompt that user gives """
#     userprompt = (
#         f"foodtype: {c2.foodtype}\n"
#         f"summary: {c2.summary}\n"
#         f"ingridients:{','.join(c2.ingridients)}"
#     )

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
