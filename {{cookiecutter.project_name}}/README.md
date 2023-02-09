# {{cookiecutter.project_name}}

## Requirements

* Docker
* Docker Compose
* Node.js v18+ (with **npm**, **nvm**)

## Backend local development

### Start the backend

* Go to the directory {{cookiecutter.project_name}}/backend

* Build image `docker build -t {{cookiecutter.project_name}}-backend .`

* Deploy `docker run -it --rm --env-file .env --name {{cookiecutter.project_name}}-backend -v ${PWD}:/var/www/{{cookiecutter.project_name}} -p 127.0.0.1:4000:80 {{cookiecutter.project_name}}-backend`

### Details

Swagger UI: http://localhost:4000/docs

ReDoc: http://localhost:4000/redoc

