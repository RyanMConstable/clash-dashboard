FROM python:3.12

WORKDIR /backend

COPY main.py /backend

RUN pip install sqlalchemy psycopg2 fastapi[standard]

CMD ["fastapi", "dev", "main.py"]
