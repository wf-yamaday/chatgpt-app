FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY ./assets/dist /app/assets/dist
COPY ./assets/templates /app/assets/templates
COPY ./src /app/src

RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
