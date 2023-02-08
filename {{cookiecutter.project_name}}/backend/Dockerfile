FROM python:3.11

COPY . /var/www/file-sign

RUN pip install --upgrade pip && pip install --no-cache-dir -r /var/www/file-sign/requirements.txt

WORKDIR /var/www/file-sign/file-sign

EXPOSE 80

CMD ["python", "./main.py"]