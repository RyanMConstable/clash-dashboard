FROM python:3.12

WORKDIR /cron

COPY clashCurl.py /cron

COPY config.py /cron

RUN pip install requests sqlalchemy psycopg2 python-dotenv

CMD ["python", "clashCurl.py"]
