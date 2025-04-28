from fastapi import FastAPI
from veel_internship.routes import recipe_router
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

app.include_router(recipe_router.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
