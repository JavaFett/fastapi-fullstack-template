FROM python:3.11

COPY . /var/www/{{cookiecutter.project_name}}

RUN pip install --upgrade pip && pip install --no-cache-dir -r /var/www/{{cookiecutter.project_name}}/requirements.txt

WORKDIR /var/www/{{cookiecutter.project_name}}/app/

EXPOSE 80

CMD ["python", "./main.py"]