from fastapi import FastAPI
from veel_internship.routes import recipe_router
from veel_internship.configs.logging_config import setup_logging
import logging
import coloredlogs



app = FastAPI(title="Recipe Generator", description="FastAPI for recipe generator")

app.include_router(recipe_router.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
