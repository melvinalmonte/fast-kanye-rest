from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from yeezy_api import config
from yeezy_api.api import router
from yeezy_api.common.logger import logger

app_config = config.get_config()


def create_app():
    logger.info('Starting Ye\'s App')
    app = FastAPI(
        title=app_config.APP_TITLE,
        version=app_config.APP_VERSION,
        docs_url=app_config.DOCS_URL,
        openapi_url=app_config.OPEN_API_URL,
        on_startup=[create_app]
    )
    app.include_router(router, prefix='/api')

    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_config.BACKEND_CORS_ORIGIN,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
