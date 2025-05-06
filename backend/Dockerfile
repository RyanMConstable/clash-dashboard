FROM python:3.12

RUN pip install sqlalchemy psycopg2 fastapi[standard] requests

WORKDIR /backend

COPY main.py /backend

COPY config.py /backend

CMD ["fastapi", "dev", "main.py"]
