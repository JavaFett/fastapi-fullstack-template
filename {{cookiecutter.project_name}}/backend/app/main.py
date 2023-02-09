import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import api
from settings import settings


app = FastAPI(
    title='{{cookiecutter.project_name}}',
    description='{{cookiecutter.project_short_description}}',
    version='{{cookiecutter.version}}',
)

app.include_router(api.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
def service_start():
    pass


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port=settings['server_port'],
        host=settings['server_host'],
        reload=settings['server_reload']
    )
