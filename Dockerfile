FROM python:3.11-alpine

WORKDIR /app

COPY ./python-project-example/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./python-project-example .

CMD ["python", "app.py"]