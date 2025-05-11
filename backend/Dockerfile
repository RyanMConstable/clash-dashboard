FROM python:3.12

EXPOSE 8000

RUN pip install sqlalchemy psycopg2 fastapi[standard] requests

WORKDIR /backend

COPY main.py /backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
