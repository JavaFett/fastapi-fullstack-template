# Fullstack fastapi app template using cookiecutter

## How to use it

Go to the directory where you want to create your project and run:

```
pip install cookiecutter
cookiecutter https://github.com/JavaFett/fastapi-fullstack-template
```

## Input variables

The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* `project_name` - The name of the project

* `project_short_description` - Short description of the project

* `version` - Starter version of the project

* `use_frontend` - Necessary to initialize the template for the frontend

* `local_db_host` - Database host

* `local_db_port` - Database port

* `local_db_dbname` - Database name

* `local_db_user` - Database login

* `local_db_password` - Database password

## Details
After creating the project **uncomment** the connection to the desired database in [db configuration file][1]

Will also appear new [`README.md`][2] file with deployment instructions, etc.

[1]: ./{{cookiecutter.project_name}}/backend/app/db/local_db.py
[2]: ./{{cookiecutter.project_name}}/README.md