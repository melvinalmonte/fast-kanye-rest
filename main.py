from fastapi import Depends
from yeezy_api import config
from yeezy_api.api import router
from yeezy_api.app import create_app
from yeezy_api.utils.utils import default_headers_injection

app_config = config.get_config()
app = create_app()
app.include_router(router, dependencies=[Depends(default_headers_injection)])
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=app_config.APP_PORT, reload=False)
