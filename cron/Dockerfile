FROM python:3.12

WORKDIR /cron

COPY clashCurl.py /cron

RUN pip install requests sqlalchemy psycopg2

CMD ["python", "clashCurl.py"]
